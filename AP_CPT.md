# AP CSP Create Performance Task — Password Generator

## 프로그램 개요

사용자의 이름, 좋아하는 것, 나이를 입력받아 개인화된 비밀번호를 생성하는 프로그램입니다.  
4자리 또는 8자리 길이를 선택할 수 있으며, 입력값의 문자들을 조합해 비밀번호를 만들어냅니다.

---

## 코드 구조

### 이벤트 핸들러

| 버튼 ID | 동작 |
|---------|------|
| `btn4` | `generate(4)` 호출 → 4자리 비밀번호 생성 |
| `btn8` | `generate(8)` 호출 → 8자리 비밀번호 생성 |
| `backBtn` | `screen1`으로 돌아가기 |

---

### 핵심 함수: `generate(length)`

```javascript
function generate(length) {
  var name = getText("nameInput");
  var fav  = getText("favInput");
  var age  = getText("ageInput");

  // 빈 입력 처리
  if (name == "") { name = "_"; }
  if (fav  == "") { fav  = "_"; }
  if (age  == "") { age  = "_"; }

  // 각 입력에서 랜덤 문자 1개씩 선택
  var password = "";
  password += name[randomNumber(0, name.length - 1)];
  password += fav[randomNumber(0, fav.length - 1)];
  password += age[randomNumber(0, age.length - 1)];

  // 나머지 자리를 채우기 위한 charList 생성
  var combined = name + fav + age;
  var charList = [];
  for (var i = 0; i < combined.length; i++) {
    appendItem(charList, combined[i]);
  }

  // length에 맞게 나머지 문자 추가
  for (var j = password.length; j < length; j++) {
    var index = randomNumber(0, charList.length - 1);
    password += charList[index];
  }

  setText("resultText", "Your password: " + password);
  setScreen("screen2");
}
```

---

## CPT 6가지 요구사항 대응

### 1. Program Purpose and Function
- **목적 (Purpose):** 사용자의 개인 정보를 기반으로 기억하기 쉬운 비밀번호를 생성
- **기능 (Function):** 이름, 좋아하는 것, 나이 텍스트를 입력받아 선택한 길이(4 또는 8)의 비밀번호를 출력
- **Input:** 세 개의 텍스트 필드 입력값 + 버튼 클릭
- **Output:** `screen2`에 표시되는 비밀번호 문자열

### 2. Data Abstraction
- **리스트:** `charList`
- **저장:** `appendItem(charList, combined[i])` 으로 문자들을 순서대로 저장
- **사용:** `charList[index]`를 통해 랜덤 인덱스로 비밀번호에 문자 추가
- **의미:** 세 입력값을 합친 문자열의 각 문자를 담은 컬렉션

### 3. Managing Complexity
- `charList`가 없다면 `combined`의 각 문자를 `char0`, `char1`, `char2` ... 등 개별 변수로 관리해야 함
- 입력 길이가 달라질 때마다 변수 개수도 달라지므로 유지보수 불가
- 리스트를 사용함으로써 임의 길이의 입력도 반복문 하나로 처리 가능

### 4. Procedural Abstraction
- **프로시저:** `generate(length)`
- **파라미터:** `length` — 비밀번호의 목표 길이를 결정하며, 이 값에 따라 반복문의 종료 조건이 바뀜
- **호출:** `btn4` 클릭 시 `generate(4)`, `btn8` 클릭 시 `generate(8)`

### 5. Algorithm Implementation
`generate` 함수 내부에 세 가지 알고리즘 요소가 모두 포함됨:

| 요소 | 위치 |
|------|------|
| **Sequencing** | 입력 읽기 → 빈값 처리 → 초기 문자 추출 → 리스트 생성 → 나머지 채우기 → 화면 출력 순서로 실행 |
| **Selection** | `if (name == "") { name = "_"; }` 등 빈 입력 처리 분기 |
| **Iteration** | `for (var i ...)` 리스트 채우기, `for (var j ...)` 비밀번호 완성 루프 |

### 6. Testing

| 호출 | 인자 | 조건 | 예상 결과 |
|------|------|------|-----------|
| `generate(4)` | name="Alice", fav="cat", age="17" | if 분기 미실행 (입력값 존재) | "Your password: " + 4자리 문자열 출력 |
| `generate(8)` | name="", fav="", age="" | if 분기 실행 (모든 입력 공백 → `"_"` 대체) | "Your password: ____" (언더스코어 기반 8자리) |

---

## 제출 체크리스트

- [ ] PPR 스크린샷: `generate` 함수 정의부
- [ ] PPR 스크린샷: `generate(4)`, `generate(8)` 호출부
- [ ] PPR에 **주석 없음** 확인
- [ ] 영상: 1분 이내, 음성 없음, 입력 및 출력 화면 포함
- [ ] 전체 코드 PDF 제출
- [ ] AI 생성 코드 사용 시 주석으로 명시
