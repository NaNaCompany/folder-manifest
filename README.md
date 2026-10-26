# 폴더 납품 목록 생성

브라우저가 제공한 파일의 상대 경로, 확장자, 바이트 크기, 수정시각(UTC), 선택적 SHA-256을 CSV·Markdown으로 내보내는 독립 정적 앱입니다. `dist/index.html`이 진입점이며 설치·빌드·서버 API가 필요 없습니다. HTTPS 또는 localhost에서 여세요.

## 사용

1. 폴더 또는 여러 파일을 선택하거나 예제로 체험합니다.
2. 점(.) 이름 제외와 SHA-256 옵션을 정합니다.
3. 목록 생성 후 CSV 또는 Markdown을 다운로드합니다. 원본 파일을 변경하지 않습니다.

## 한계

- 최대 2,000파일, 합계 500 MiB. SHA-256은 파일당 100 MiB까지 지원합니다.
- 폴더 선택은 브라우저 지원에 따라 다릅니다. 파일 선택 시 상대 폴더 경로가 제공되지 않습니다.
- 운영체제 숨김 속성은 확인할 수 없습니다. 점(.)으로 시작하는 경로 구성요소만 선택적으로 제외합니다. 빈 폴더와 브라우저가 전달하지 않은 파일은 목록에 없습니다.
- 테이블 미리보기는 300행이며 전체 다운로드는 최대 2,000행입니다.
- CSV는 UTF-8 BOM, CRLF, RFC 4180 인용 규칙을 사용합니다. 수식 보호를 켜면 공백 뒤 `= + - @`로 시작하는 값에 작은따옴표를 붙입니다.
- 파일 읽기·해시는 브라우저 메모리를 사용합니다. 결과는 새로고침 후 복구되지 않습니다.
- 실제 브라우저 조작·시각 QA는 수행하지 않았습니다. 소스·fixture 검증 완료 상태입니다.

## 검증

2026-10-26 실행. RTK proxy로 번들 Node를 호출했습니다. 아래의 `$rtk`와 `$node`는 실행 환경의 해당 실행 파일 절대 경로입니다. 개인 경로를 아티팩트에 포함하지 않기 위해 기호로 표시합니다.

```powershell
& $rtk proxy $node --check dist/app.js
& $rtk proxy $node --test test.mjs
```

결과: 문법 검사 exit 0. Node test 4개 통과, 실패 0. 확장자·숨김 구성요소, 빈 입력·개수·용량 상한, CSV 인용부호/줄바꿈/수식 보호, Markdown 특수문자, SHA-256 빈 문자열·abc 표준 fixture를 검증했습니다.

## 출처

- W3C Web Cryptography API: https://www.w3.org/TR/WebCryptoAPI/
- RFC 4180 CSV: https://www.rfc-editor.org/rfc/rfc4180

UI·코드·예제는 이 앱을 위해 작성한 원본입니다. 외부 폰트·라이브러리·이미지·추적 코드가 없습니다.

## 6개 언어
한국어 루트 및 /en/, /es/, /zh/, /ja/, /de/ 지원. 모든 경로의 언어 메뉴는 사용자가 직접 전환합니다. UI·오류·상태·도움말·내보내기 헤더는 로컬 사전으로 번역하며 파일명·파일내용은 번역하지 않습니다. build_locales.py는 배포 전 정적 경로를 재생성하는 선택적 개발 도구입니다. 배포 시 빌드는 필요 없습니다. 추가 검증 후 Node test 5개 통과, 실패 0. 6개 경로의 lang·noindex·언어메뉴와 모든 data-t 키의 번역 존재를 검증했습니다.

## Public GitHub Pages release

Launch: https://nanalab.kr/folder-manifest/

Korean is at the root. English, Spanish, Chinese, Japanese and German use `/en/`, `/es/`, `/zh/`, `/ja/`, `/de/`.
GitHub Pages serves `main` → `/docs` using the branch build. No project CNAME is used.

Build: `node scripts/build-public.mjs`. The `dist/` snapshot and its original generators/tests are preserved as the application source. The public build adds metadata, six-locale sitemaps, original JPEG cards, More Apps styling and the existing NaNa publisher integrations. It does not upload selected user files.

Publisher integrations: AdSense, Google Tag Manager, Google Analytics and Cloudflare Web Analytics, with the same publisher settings as the NaNa Lab homepage. These scripts can make network requests independently of local file processing.

Original JPEG cards are rendered from original text and geometry using an installed system font; no font files are redistributed. Existing source references and third-party notices remain applicable.
