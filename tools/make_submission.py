#!/usr/bin/env python3
"""'AX 인재전쟁 2026' 예선 제출용 submission.zip 패키징 스크립트.

사용법:
    python tools/make_submission.py <slug>

slug: channeltalk | musinsa | kakaopay-securities

생성물: dist/<slug>/submission.zip
    submission.zip
    ├── src/        <- <slug>/src/ 전체
    │   ├── examples/  <- <slug>/examples/ 사본 (실제 예시 산출물 — 심사자가 zip만 열어도 확인 가능)
    │   └── docs/      <- <slug>/docs/ 핵심 문서 사본 (리서치·검증·답변·영상 자막)
    ├── README.md   <- <slug>/README.md
    └── logs/       <- repo 로그와 <slug> 로그를 원본 파일명 유지해 분리 보관

공고 스펙의 최상위 구조(src/README/logs)를 유지하고, 추가 근거는 스펙이
"구조 자유"라고 명시한 src/ 아래에 사본으로 포함한다.

표준 라이브러리만 사용하며 Windows 경로와 호환됩니다.
"""
import os
import sys
import zipfile

# Windows 콘솔/파이프에서도 한국어 메시지가 깨지지 않도록 UTF-8로 강제한다.
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

VALID_SLUGS = ("channeltalk", "musinsa", "kakaopay-securities")
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# zip의 src/docs/ 에 사본으로 넣을 핵심 문서 (존재하는 것만 포함)
EXTRA_DOC_FILES = (
    "research.md",
    "output-spec.md",
    "verification.md",
    "engineering.md",
    "submission-answers.md",
    "source-video.ko.vtt",
)


def _iter_files(src_dir):
    """src_dir 아래 모든 파일 경로를 정렬된 순서로 순회한다."""
    for dirpath, dirnames, filenames in os.walk(src_dir):
        dirnames.sort()
        for filename in sorted(filenames):
            yield os.path.join(dirpath, filename)


def _add_tree(zf, src_dir, arc_prefix, written, skip_names=()):
    """src_dir 전체를 zip의 arc_prefix/ 아래로 추가한다. 추가한 파일 수를 반환."""
    count = 0
    for full_path in _iter_files(src_dir):
        if os.path.basename(full_path) in skip_names:
            continue
        rel = os.path.relpath(full_path, src_dir)
        arcname = arc_prefix + "/" + rel.replace(os.sep, "/")
        if arcname in written:
            print(f"경고: zip 내 경로 중복으로 건너뜀: {arcname}")
            continue
        zf.write(full_path, arcname)
        written.add(arcname)
        count += 1
    return count


def main(argv):
    if len(argv) != 2 or argv[1] not in VALID_SLUGS:
        print("사용법: python tools/make_submission.py <slug>", file=sys.stderr)
        print(f"  slug: {' | '.join(VALID_SLUGS)}", file=sys.stderr)
        return 1

    slug = argv[1]
    slug_dir = os.path.join(REPO_ROOT, slug)
    src_dir = os.path.join(slug_dir, "src")
    readme_path = os.path.join(slug_dir, "README.md")
    plugin_json = os.path.join(src_dir, ".codex-plugin", "plugin.json")

    if not os.path.isfile(plugin_json):
        print(f"에러: 필수 파일이 없습니다: {plugin_json}", file=sys.stderr)
        return 1
    if not os.path.isfile(readme_path):
        print(f"에러: 필수 파일이 없습니다: {readme_path}", file=sys.stderr)
        return 1

    out_dir = os.path.join(REPO_ROOT, "dist", slug)
    os.makedirs(out_dir, exist_ok=True)
    out_zip = os.path.join(out_dir, "submission.zip")

    written = set()
    log_count = 0
    extra_count = 0
    with zipfile.ZipFile(out_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        _add_tree(zf, src_dir, "src", written)
        # 심사자가 zip만 열어도 예시 산출물과 핵심 근거 문서를 볼 수 있도록
        # src/ 아래에 사본으로 포함한다 (스펙: src 내부 구조는 자유).
        examples_dir = os.path.join(slug_dir, "examples")
        if os.path.isdir(examples_dir):
            extra_count += _add_tree(zf, examples_dir, "src/examples", written)
        docs_dir = os.path.join(slug_dir, "docs")
        for doc_name in EXTRA_DOC_FILES:
            doc_path = os.path.join(docs_dir, doc_name)
            if os.path.isfile(doc_path):
                arcname = "src/docs/" + doc_name
                if arcname not in written:
                    zf.write(doc_path, arcname)
                    written.add(arcname)
                    extra_count += 1
        zf.write(readme_path, "README.md")
        written.add("README.md")
        zf.writestr("logs/", "")  # logs/ 폴더 엔트리 (비어 있어도 구조 유지)
        log_sources = (
            (os.path.join(REPO_ROOT, "logs"), "logs/repo"),
            (os.path.join(slug_dir, "logs"), f"logs/{slug}"),
        )
        for logs_dir, logs_arc_prefix in log_sources:
            if os.path.isdir(logs_dir):
                log_count += _add_tree(zf, logs_dir, logs_arc_prefix, written,
                                       skip_names=(".gitkeep",))

    if log_count == 0:
        print("경고: logs/ 에 로그 파일이 없습니다. AI 대화 로그 원본은 제출 필수이며 "
              "없으면 실격 사유가 될 수 있습니다. (패키징은 계속 진행됨)")

    print(f"생성 완료: {out_zip}")
    print(f"  - src/ 파일 및 README.md 포함, 로그 파일 {log_count}개 포함")
    print(f"  - src/examples·src/docs 사본 {extra_count}개 포함 (예시 산출물·핵심 근거)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
