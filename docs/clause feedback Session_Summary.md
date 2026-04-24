# AP CSP Create Performance Task - 세션 정리

> **작성 목적**: Password Generator 프로그램의 AP CSP CPT 루브릭 최적화 과정 기록
> **프로그램**: Password Generator (App Lab JS → Python 변환)
> **최종 목표**: 시험(Written Response) 유리함 극대화

---

## 1. 프로그램 개요

### 1-1. 원본 JavaScript (App Lab)
```javascript
onEvent("btn4", "click", function() { generate(4); });
onEvent("btn8", "click", function() { generate(8); });

function generate(length) {
  var name = getText("nameInput");
  var fav = getText("favInput");
  var age = getText("ageInput");

  if (name == "") { name = "_"; }
  if (fav == "")  { fav = "_";  }
  if (age == "")  { age = "_";  }

  var password = "";
  password += name[randomNumber(0, name.length - 1)];
  password += fav[randomNumber(0, fav.length - 1)];
  password += age[randomNumber(0, age.length - 1)];

  var combined = name + fav + age;
  var charList = [];
  for (var i = 0; i < combined.length; i++) {
    appendItem(charList, combined[i]);
  }
  for (var j = password.length; j < length; j++) {
    var index = randomNumber(0, charList.length - 1);
    password += charList[index];
  }

  setText("resultText", "Your password: " + password);
  setScreen("screen2");
}
```

### 1-2. 원본 Python 변환
매개변수 1개(`length`), `charList`(combined 문자열의 단순 복사본) 사용.

---

## 2. 핵심 루브릭 기준 3가지

### Row 3: List & Complexity Management
**College Board 공식 요구사항:**
> "The data abstraction must make the program easier to develop (alternatives would be more complex) or easier to maintain (future changes to the size of the list would otherwise require significant modifications to the program code)."

**즉, 리스트가 다음 중 하나를 증명해야 함:**
- (a) 리스트 없으면 **개발이 더 복잡**해짐 (대안이 더 복잡함)
- (b) 리스트 크기 변경 시 **유지보수가 어려워짐** (대규모 수정 필요)

### Row 5: Procedural Abstraction
- 매개변수가 프로시저의 기능에 영향을 미쳐야 함
- "one or more parameters" (1개여도 통과는 가능, 2개가 더 유리)

### Row 6: Testing with Different Arguments
> "Each call must pass a different argument(s) that causes a **different segment of code** in the procedure to execute."

**즉, 서로 다른 인자값이 서로 다른 코드 구간(if 분기 등)을 실행시켜야 함.**
반복 횟수만 바꾸는 매개변수는 불충분함.

---

## 3. 원본 코드의 문제점 분석

### 3-1. `charList` 문제 (Row 3 위험)

원본 `charList`는 `combined` 문자열을 그대로 리스트에 복사한 것.

**문제:**
- Python/JS에서 문자열은 이미 인덱스 접근 가능 (`combined[i]`)
- `charList`를 제거해도 **똑같이 작동함**
- 오히려 `charList` 없는 버전이 **더 짧고 단순**

**대안 비교:**
| 버전 | 줄 수 | 기능 |
|------|------|------|
| charList 있음 (원본) | 7줄 | 동일 |
| charList 없음 (대안) | 4줄 | 동일 |

→ 루브릭의 "alternatives would be more complex"에 **정반대**로 작용.
→ 채점자가 "복잡성 관리 목적 불명확"으로 판단할 위험 높음.

### 3-2. `length` 매개변수 문제 (Row 6 위험)

`generate(4)`와 `generate(8)`은:
- **같은 for 루프**를 실행함 (단지 반복 횟수만 다름)
- "different segment of code"를 실행하는 게 아님

→ Row 6 testing 기준을 충족한다고 보기 어려움.

---

## 4. 의사결정 과정

### 4-1. 고려한 옵션들

| 옵션 | 매개변수 | 리스트 | 평가 |
|------|---------|--------|------|
| A: 길이 고정 (8자리만) | `generate(use_special)` | `symbols` | 매개변수 1개, 할 말 적음 |
| **B: 길이 + 특수기호** ✅ | `generate(length, use_special)` | `symbols` | 매개변수 2개, 원본 의도 보존 |
| C: Gemini 원안 | `generate(length, use_special)` (6/8) | `symbols` | 원본 선택지 4/8 → 6/8 변경됨 |

### 4-2. 최종 선택: **옵션 B** (시험 유리함 최우선)

**선택 이유:**
1. **매개변수 2개** → Procedural Abstraction이 더 명확히 드러남
2. **원본 4자리/8자리 선택지 보존** → 불필요한 변경 최소화
3. **Written Response에서 할 말 풍부** → 입력 5가지, 기능 설명 풍성
4. **프로그램 목적이 "사용자 맞춤형 보안 도구"로 격상** 가능

### 4-3. 4/8 길이 유지가 가능한 이유

특수기호는 **1개만** 추가하면 논리 충돌 없음:
- 4자리 + "yes": 3글자(name/fav/age) + 1특수 = **4글자 정확**
- 4자리 + "no": 3글자 + while 루프로 1글자 = 4글자
- 8자리 + "yes": 3글자 + 1특수 + while 루프 4글자 = 8글자
- 8자리 + "no": 3글자 + while 루프 5글자 = 8글자

---

## 5. 최종 확정 코드

```python
import random

def generate(length, use_special):
    name = input("Name: ")
    fav  = input("Favorite thing: ")
    age  = input("Age: ")

    if name == "": name = "_"
    if fav  == "": fav  = "_"
    if age  == "": age  = "_"

    symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]

    password = ""
    password += name[random.randint(0, len(name) - 1)]
    password += fav[random.randint(0, len(fav) - 1)]
    password += age[random.randint(0, len(age) - 1)]

    if use_special == "yes":
        password += symbols[random.randint(0, len(symbols) - 1)]

    combined = name + fav + age
    while len(password) < length:
        password += combined[random.randint(0, len(combined) - 1)]

    print("Your password:", password)

print("=== Password Generator ===")
choice = input("Generate 4-digit or 8-digit password? (4/8): ")
special = input("Include special symbol? (yes/no): ")

if choice == "4":
    generate(4, special)
elif choice == "8":
    generate(8, special)
else:
    print("Invalid choice.")
```

---

## 6. Written Response 답안 템플릿

### 6-1. 3(c): List & Complexity Management ⭐ 핵심

**완성 답안 (Model Answer):**

> The list in my program is named `symbols`, and it stores eight special characters: `!`, `@`, `#`, `$`, `%`, `^`, `&`, and `*`. These characters are stored together in a single collection when the program begins executing.
>
> When the user selects "yes" for the special symbol option, my program uses this list by generating a random index between 0 and 7 with `random.randint(0, len(symbols) - 1)`, then accessing the character at that index with `symbols[index]`. This randomly selected symbol is appended to the password, which helps fulfill the program's purpose of creating a more secure, unpredictable password.
>
> The `symbols` list manages complexity by making my program **easier to maintain**. Without this list, I would need to declare eight separate variables such as `sym1 = "!"`, `sym2 = "@"`, and so on, and then write a long if-elif chain with eight branches to randomly select one symbol based on a random number. If I wanted to add a new symbol like `?` in the future, I would have to: (1) create a new variable, (2) change the range of the random number generator, and (3) add another elif branch. With the list, I only need to add one element to the list, and the existing code still works correctly because `len(symbols)` automatically adjusts the random range. This demonstrates that the list significantly reduces the amount of code I need to modify when the size of the data changes.

**답변 구조 3가지 포인트:**
1. **리스트에 무엇이 저장되나** (8개 특수기호 구체적 나열)
2. **프로그램 목적을 위해 어떻게 사용되나** (random index + 인덱스 접근 + append)
3. **복잡성 관리 방식** (대안: 8개 변수 + if-elif 체인 / 변경 시 3단계 vs 1줄)

### 6-2. 3(d): Procedure Testing ⭐ 핵심

**Call 1:** `generate(4, "yes")`
- Condition tested: 사용자가 특수기호 포함을 원함
- Segment executed: `if use_special == "yes":` 블록 **내부** 코드 실행 → 특수기호 추가

**Call 2:** `generate(4, "no")`
- Condition tested: 사용자가 특수기호 미포함을 원함
- Segment executed: `if` 블록 **완전히 스킵**, while 루프가 다른 segment로 실행

→ "different segments of code execute" 교과서적 예시.

### 6-3. 3(a): Program Purpose
포지셔닝: "단순 비밀번호 생성기"가 아닌 **"사용자 맞춤형 보안 도구"**
- `length`와 `use_special` 두 옵션 → 사용자 맞춤 보안 요구 대응

### 6-4. 3(b): Input/Output
- 입력 5가지: name, fav, age, choice, special
- 출력: 조합으로 생성된 비밀번호

---

## 7. 절대 쓰면 안 되는 표현 (감점 유발)

- ❌ "The list makes the code shorter" — 너무 막연함
- ❌ "Lists are useful in programming" — 일반론
- ❌ "It's more efficient" — 복잡성 관리와 무관
- ❌ "Easier to read" — 루브릭 키워드 아님 (develop/maintain만 사용)

---

## 8. 시험 준비 체크리스트

### 8-1. Component별 제출 주의사항

| Component | 주의사항 |
|-----------|---------|
| **A (Program Code PDF)** | 주석 포함 OK, 오히려 있는 게 유리 |
| **B (Video)** | 독립 작성, 파트너/AI와 협업 금지 |
| **C (PPR)** | **주석 하나라도 있으면 자동 0점** / 독립 작성 |

### 8-2. PPR 스크린샷 기술 요건
- 최소 **10pt 폰트** (12pt 권장)
- 블러리하면 안 됨 (zoom out 후 확대 금지)
- 와이드 코드 피하기 (긴 줄은 여러 줄로)
- 주석/과목 콘텐츠 제거 필수

### 8-3. PPR 리스트 스크린샷 2개
1. **저장 장면**: `symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]`
2. **사용 장면**: `password += symbols[random.randint(0, len(symbols) - 1)]` (if 블록 포함)

### 8-4. PPR 프로시저 스크린샷 2개
1. **프로시저 정의**: `def generate(length, use_special):` 전체 몸체
2. **호출부**: `generate(4, special)` / `generate(8, special)` 포함 코드

### 8-5. 암기 핵심 키워드 (Written Response용)
1. "eight special characters" — 리스트 내용
2. "random.randint + index access" — 사용 메커니즘
3. "eight separate variables + if-elif chain" — 대안 복잡성
4. "add one element + len() auto-adjusts" — 유지보수 단순화
5. "significant modifications" — 루브릭 핵심 문구 직접 인용

---

## 9. Academic Integrity 주의사항

### 9-1. AI 사용 허용 범위
- ✅ 루브릭 이해, 코딩 원리 학습, 디버깅 도움
- ✅ **본인의** 코드 개발 과정에서 AI 활용
- ❌ AI가 작성한 코드를 출처 표기 없이 제출 (플래그리즘)
- ❌ PPR/영상 작성 과정에서 AI/타인 협업

### 9-2. 협업 허용 범위
- ✅ Component A (프로그램 코드): 공식 파트너와 협업 가능
- ❌ Component B (영상): 독립 작성
- ❌ Component C (PPR): 독립 작성

### 9-3. 위반 시 결과
- 플래그리즘 → **자동 0점** (Written Response 포함)
- PPR에 주석 포함 → **자동 0점**

---

## 10. 다음 세션에서 다른 학생 코드 검토 시

### 10-1. 새 세션 첫 메시지 템플릿

```
AP CSP Create Performance Task 검토를 부탁해.

핵심 검토 기준:
1. Row 3 (List & Complexity): 리스트가 "대안이 더 복잡함" 또는 
   "유지보수 시 대규모 수정 필요"를 실제로 충족하는지. 
   문자열을 리스트로 단순 복사하는 패턴은 감점 위험.
2. Row 5/6 (Procedural Abstraction & Testing): 매개변수가 
   반복 횟수만 바꾸는 게 아니라, 서로 다른 코드 segment 
   (예: if 분기)를 실행시키는 구조인지.
3. PPR 스크린샷 금지사항: 주석 하나라도 있으면 자동 0점.

이 학생의 원본 코드: [붙여넣기]
프로그램 목적: [설명]
검토 목적: [본인 코드 / 파트너 공동 개발 / 기타]
```

### 10-2. 검토 성격별 가능 여부

| 성격 | 가능 여부 |
|------|-----------|
| 본인(Josh) 코드 검토 | ✅ 자유롭게 |
| 공식 파트너 공동 개발 코드 | ✅ Component A까지만 |
| 동급생 코드를 대신 AI로 개선 | 🚨 플래그리즘 위험 |
| 교사/멘토 입장의 루브릭 피드백 | ✅ 루브릭 이해 돕는 용도 OK |

---

## 11. 참고 자료 (프로젝트 내 문서)

- `apcspstudenttaskdirections.pdf` — 공식 Student Task Directions
- `apcsppersonalizedprojectreferencetipsheet.pdf` — PPR 팁시트 (7p)
- `What is the academic integrity and plagiarism policy_.html` — 학업 정직성 정책
- `apdigitalportfoliotermsandconditions.pdf` — AP Digital Portfolio 이용약관
- `apdigitalportfoliostudentuserguide.pdf` — Student User Guide

---

## 12. 세션 핵심 교훈 (한 줄 요약)

> **"리스트를 쓰는 것"과 "리스트로 복잡성을 관리하는 것"은 다르다.**
> 루브릭은 전자가 아니라 후자를 평가한다.
> 리스트가 없어도 같은 기능이 가능한가?를 자문해야 한다.
