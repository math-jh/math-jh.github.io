#!/usr/bin/env python3
"""영상 같은 큰 파일을 Cloudflare R2 버킷에 올린다. 글에서는 _includes/video.html 로 부른다.

버킷: math-jh-media, 공개 주소: https://media.math-jh.com/<키>
자격 증명: ~/.config/r2-media/r2.env (레포 밖, chmod 600). 이 버킷만 읽고 쓰는 R2 API 토큰이다.

  R2_ACCOUNT_ID=...
  R2_ACCESS_KEY_ID=...
  R2_SECRET_ACCESS_KEY=...
  R2_BUCKET=math-jh-media

  python3 scripts/media/r2_upload.py --prefix keyboards/ a.mp4 b.mp4   # 올리기 (같은 크기면 건너뜀)
  python3 scripts/media/r2_upload.py --force --prefix keyboards/ a.mp4 # 덮어쓰기
  python3 scripts/media/r2_upload.py --list                            # 버킷 목록

같은 키를 덮어쓰면 Cloudflare 캐시에 옛 파일이 max-age 동안 남는다. 바뀐 영상은 새 이름으로 올린다.
"""

import argparse
import mimetypes
import sys
from pathlib import Path

import boto3
from botocore.config import Config

ENV = Path.home() / ".config/r2-media/r2.env"
PUBLIC = "https://media.math-jh.com"
CACHE_CONTROL = "public, max-age=2592000"  # 30일


def load_env():
    if not ENV.is_file():
        sys.exit(f"자격 증명 파일이 없다: {ENV}")
    env = {}
    for line in ENV.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip().strip("'\"")
    missing = [k for k in ("R2_ACCOUNT_ID", "R2_ACCESS_KEY_ID", "R2_SECRET_ACCESS_KEY", "R2_BUCKET") if not env.get(k)]
    if missing:
        sys.exit(f"{ENV} 에 빠진 값: {', '.join(missing)}")
    return env


def client(env):
    return boto3.client(
        "s3",
        endpoint_url=f"https://{env['R2_ACCOUNT_ID']}.r2.cloudflarestorage.com",
        aws_access_key_id=env["R2_ACCESS_KEY_ID"],
        aws_secret_access_key=env["R2_SECRET_ACCESS_KEY"],
        region_name="auto",
        config=Config(request_checksum_calculation="when_required",
                      response_checksum_validation="when_required"),
    )


def remote_size(s3, bucket, key):
    try:
        return s3.head_object(Bucket=bucket, Key=key)["ContentLength"]
    except s3.exceptions.ClientError as e:
        if e.response.get("Error", {}).get("Code") in ("404", "NoSuchKey", "NotFound"):
            return None
        raise


def upload(s3, bucket, files, prefix, force):
    for f in map(Path, files):
        if not f.is_file():
            sys.exit(f"파일이 없다: {f}")
        key = prefix + f.name
        size = f.stat().st_size
        if not force and remote_size(s3, bucket, key) == size:
            print(f"건너뜀 (같은 크기가 이미 있음): {key}")
            continue
        ctype = mimetypes.guess_type(f.name)[0] or "application/octet-stream"
        s3.upload_file(str(f), bucket, key,
                       ExtraArgs={"ContentType": ctype, "CacheControl": CACHE_CONTROL})
        if remote_size(s3, bucket, key) != size:
            sys.exit(f"올린 뒤 크기가 다르다: {key}")
        print(f"올림 {size / 1048576:6.1f} MB  {PUBLIC}/{key}")


def list_objects(s3, bucket):
    n = total = 0
    for page in s3.get_paginator("list_objects_v2").paginate(Bucket=bucket):
        for o in page.get("Contents", []):
            n += 1
            total += o["Size"]
            print(f"{o['Size'] / 1048576:8.1f} MB  {o['Key']}")
    print(f"{n} 개, {total / 1048576:.1f} MB")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*")
    ap.add_argument("--prefix", default="", help="버킷 안 폴더, 끝에 / (예: keyboards/)")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()
    if a.prefix and not a.prefix.endswith("/"):
        a.prefix += "/"
    env = load_env()
    s3 = client(env)
    if a.list:
        list_objects(s3, env["R2_BUCKET"])
    elif a.files:
        upload(s3, env["R2_BUCKET"], a.files, a.prefix, a.force)
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
