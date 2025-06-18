# TodoList(Bedrock)

TodoList 서비스의 백앤드입니다.  
FastAPI와 MongoDB를 사용하며, 사용자 인증(회원가입, 로그인, 로그아웃, Google OAuth) 및 할 일 CRUD 기능을 제공합니다.  

---

## 주요 기능

- **사용자 인증**
  - 회원가입
  - 로그인
  - 로그아웃
  - Google OAuth 로그인
- **할 일 관리**
  - 할 일 생성
  - 할 일 조회
  - 할 일 수정
  - 할 일 삭제

---

## 기술 스택

- **프레임워크**: FastAPI
- **데이터베이스**: MongoDB
- **인증**: OAuth2, JWT
- **패키지 관리**: uv, pip

---

## 프로젝트 구조

backend/  
├── main.py # FastAPI 앱 진입점  
│  
├── core/ # 공통 기능  
│ ├── config.py # 환경 변수, 설정  
│ ├── database.py # MongoDB 연결  
│ └── security.py # 보안 관련 (OAuth2, JWT 등)  
│  
├── auth/ # 인증 관련 모듈  
│ ├── init.py    
│ ├── models.py # 유저 모델  
│ ├── schemas.py # 유저, 토큰 스키마  
│ ├── routes.py # 인증 라우터 (회원가입, 로그인, 로그아웃, Google OAuth)  
│ └── dependencies.py # 의존성/권한 체크  
│  
└── todos/ # 할 일 관련 모듈  
├── init.py  
├── models.py # Todo 모델  
├── schemas.py # Todo 스키마  
├── routes.py # Todo CRUD 라우터  
└── services.py # Todo 비즈니스 로직  

