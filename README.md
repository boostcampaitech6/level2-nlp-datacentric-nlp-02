# 🏆**Level2 Project - TC(Topic Classification)**


## ✏️**대회 소개**

<div align='center'>

|특징|설명|
|:--:|--|
|**대회 주체**|네이버 커넥트 재단 부스트캠프 AI Tech 6기 NLP트랙의 level2 실전 프로젝트 대회입니다.|
|**대회 설명**|모델 구조의 변경 없이 데이터적 관점에서 뉴스 제목의 주제를 분류하는 모델을 학습하는 Task입니다.|
|**데이터 구성**|데이터는 KLUE-YNAT 데이터로, 뉴스 헤드라인과 해당 기사의 주제가 라벨링되어 있습니다. Train(7,000개), Test(47,785개) |
|**평가 지표**| KLUE Topic Classification의 Evaluation metrics를 똑같이 사용했습니다. 각 Label 별 F1-score 계산 후 모든 Label에 대한 평균을 계산하는 macro F1 점수로 평가합니다.|
</div>


<br>

## 👨‍💻Team & Members

**더닝크루거 [NLP 2조]**


### 🧚**Members**

<div align='center'>

|구다연[<img src="images/github-mark.png" width="20" style="vertical-align:middle;">](https://github.com/9ooDa)|김동현[<img src="images/github-mark.png" width="20" style="vertical-align:middle;">](https://github.com/valofosho)|김유민[<img src="images/github-mark.png" width="20" style="vertical-align:middle;">](https://github.com/miniminii)|김희범[<img src="images/github-mark.png" width="20" style="vertical-align:middle;">](https://github.com/C7C4FF)|이민아[<img src="images/github-mark.png" width="20" style="vertical-align:middle;">](https://github.com/minari1505)|이지인[<img src="images/github-mark.png" width="20" style="vertical-align:middle;">](https://github.com/Boribori12)|
|:--:|:--:|:--:|:--:|:--:|:--:|
|<img style="height:auto;" alt="View 9ooDa's full-sized avatar" src="https://avatars.githubusercontent.com/u/79597984?v=4" width="50" height="50">|<img style="height:auto;" src="https://avatars.githubusercontent.com/u/58420112?v=4" width="50" height="50">|<img style="height:auto;" src="https://avatars.githubusercontent.com/u/90626970?v=4" width="50" height="50">|<img style="height:auto;" src="https://avatars.githubusercontent.com/u/80257041?v=4" width="50" height="50">|<img style="height:auto;" src="https://avatars.githubusercontent.com/u/81675036?v=4" width="50" height="50">|<img style="height:auto;" src="https://avatars.githubusercontent.com/u/93438663?v=4" width="50" height="50">|
|[Mail](dayeonkuhk@gmail.com)|[Mail](whgdk1880@gmail.com)|[Mail](sksdjssl3148@gmail.com)|[Mail](c7c4ff.beom@gmail.com)|[Mail](minari1505@naver.com)|[Mail](sos000523@naver.com)|
</div>

<br>

## 🏃**Project Process**

### 🖥️ Project Introduction
|**개요**|**Description**|
|:--:|--|
|**프로젝트 주제** | **`TC(Topic Classification)`** : 뉴스 헤드라인을 보고 해당 기사에 맞는 주제로 분류|
|**프로젝트 목표**| 모델 구조의 변경 없이, Data-Centric 관점에서 다양한 전처리 및 증강을 실험해보며 성능을 개선|
|**프로젝트 평가지표**|각 Label 별 F1-score 계산 후 모든 Label에 대한 평균을 계산하는 macro F1 점수로 평가|
|**프로젝트 기간**| `2024-01-24 ~ 2024-02-01` 약 9일간 진행|
|**개발 환경**|**`GPU` : Tesla V100 Server 6대**, **`IDE` : Vscode, Jupyter Notebook**|
|**협업 환경**|**`Notion`**(진행 상황 공유), **`Github`**(코드 및 데이터 공유), **`Slack`**(실시간 소통) |

<br>

### 📋**Data**

**데이터셋**

| 데이터 | 사용 데이터셋 | 목적 | 구성 |
| --- | --- | --- | --- |
| 학습 데이터 | train.csv, 7,000개 | 학습 데이터 셋을 활용한 학습 모델 생성 | 샘플 고유번호(ID), 분류 대상 텍스트-연합뉴스기사 헤드라인(text), 정수로 인코딩된 라벨(target), 해당 데이터의 url(url), 해당 데이터 작성 날짜 및 시간(date) |
| 평가 데이터 | test_data.csv, 47,785개 | 학습된 모델에 기반한 문장의 주제(target) 예측 | 샘플 고유번호(ID), 분류 대상 텍스트-연합뉴스기사 헤드라인(text), 해당 데이터의 url(url), 해당 데이터 작성 날짜 및 시간(date) |

**예시**        
| text | target |
| --- | --- |
| 삼성전자 KBIS 2018서 세프컬렉션 선보여 | 0 - IT과학 |
| 개포2단지 분양 앞두고 개포지구 재건축 불붙어 | 1 - 경제 |
| 증명사진 없어도 재외공관서 전자여권 신청 가능 | 2 - 사회 |
| 신간 블록체인혁명 2030·남자의 고독사 | 3 - 문화 |
| 美웨스트버지니아 경선 샌더스 박빙 우세…전체 판세와는 무관 | 4 - 세계 |
| 월드컵 주장 기성용은 왜 거짓말쟁이라는 단어를 썼나 | 5 - 스포츠 |
| 황총리 안보위기 평화통일 전기되도록 할 것 | 6 - 정치 |

<br>

1. Data Distribution

   
    ![Untitled](https://github.com/boostcampaitech6/level2-nlp-datacentric-nlp-02/assets/80257041/3ac2cdde-eee7-43e5-9d69-b7974855e50d)
   
    Train 데이터는 각 라벨 당 1,000개씩 Uniform Distribution을 따르고 있습니다.

3. Data Noise
    
    Noise Data는 총 6,852개로 학습 및 평가 데이터 모두에 존재했습니다. 학습과 전체 데이터에 약 12.5% 정도를 차지하고 있습니다. 주어진 Text가 발음 규칙에 맞게 변경된 prescriptive pronunciation 40%, 실제 생활에서 주로 쉽게 발음되는 방식인 descriptive pronunciation 40%, labeling error가 20%를 차지했습니다.

   <br>

    

### 🕵️**What We Did**

* 프로젝트를 진행하며 단계별로 실험해 보고 적용해 본 내용들은 아래와 같습니다.
* 보다 자세한 사항은 [📋Wrap-up Report](https://supreme-kilogram-785.notion.site/Wrap-up-Report-Data-Centric-8117a07008da486face14618142fa027?pvs=4)를 참고해주시기 바랍니다.

### Data Preprocessing

1. Data Labeling Error Detection

    라벨링 에러를 탐색하기 위한 방법으로, 학습 데이터에 대해 전수조사를 수행, 이 결과 약 700개가량을 라벨에 노이즈가 낀 데이터로 판단했습니다.
    
    팀원 모두가 동일하게 생각한 라벨 값만 바꿔주는 만장일치, 기존 라벨값을 포함한 다수결, 팀원의 의견이 4명 이상 갈린 경우에는 기존 target 값을 따르도록 세 가지 데이터 셋을 생성했습니다.
    
    baseline 코드의 macro f1-score 0.8392를 기준으로, 만장일치는 `0.8394`로 상승하였고, target을 포함한 다수결은 `0.8340`, 기존 target 값을 따른 경우에는 `0.8374`로 감소하였습니다. 추후 실험은 만장일치로 수정된 데이터 셋을 기준으로 진행했습니다.

    ![Untitled 1](https://github.com/boostcampaitech6/level2-nlp-datacentric-nlp-02/assets/80257041/d054a568-d6e6-4992-909a-995c1fd87942)
   
4. Max Length 조절

    `text` column의 데이터를 tokenize한 후의 길이를 분포로 나타내어 분석을 진행했습니다. 분석 결과 모든 헤드라인이 32보다 짧았고, 약 99%의 데이터가 24보다 짧았습니다. 실험 결과, max length가 24일 때 기존 값인 128보다 2초 정도 빠르게 학습되는 것을 알 수 있었습니다. F1 score 향상은 없었지만, 효율적인 학습을 위해 24를 채택해 진행했습니다.
   
6. Clean Lab
   
     cleanlab 라이브러리를 활용하여 데이터 내에 존재하는 라벨 에러 탐지 및 제거 작업을 진행했습니다. 기준 score를 0.01로 설정하여 약 200개, 0.05로 설정하여 약 400개의 라벨 에러를 탐지하여 clean lab이 예측한 라벨로 대체해 주는 작업을 거쳐주었습니다. 그 결과 F1 score가 `0.8392 → 0.8397`로 성능이 향상되었습니다.
   
8. 부사 제거

     konlpy 라이브러리를 활용하여 조사, 부사, 문장 부호를 제거하는 작업을 진행했습니다. 문장 내 조사, 부사, 불용어 등 의미를 내포하지 않는 단어들을 제거해 줌으로써 주제 단어들에 대한 모델의 집중도를 높여 성능 향상을 기대하였지만, `0.8418 → 0.8381` 으로 성능이 하락하였습니다.
10. 한자 한글 변환

    hanja 라이브러리를 활용하여 한자를 한글로 음차번역하는 작업을 진행했습니다. 문장 내 한자를 한글로 음차번역하여 전체적인 문장의 통일성을 유지하는 방법을 통해 모델의 성능 향상을 기대하였지만, `0.8394 → 0.8385`로 성능이 하락하였습니다.
12. 맞춤법 교정

    hanspell 라이브러리를 이용하여 일괄적으로 맞춤법을 교정하는 작업을 진행했습니다. 데이터셋이 뉴스 헤드라인이기 때문에 큰 오류는 없었지만, 말줄임표와 같은 문장부호들이 띄어쓰기 없이 진행된 결과 등이 수정되었습니다. `0.8392 → 0.8411`로 성능 개선이 있었습니다.

    하지만, train과 dev를 8:2로 나눈 실험에서는 오히려 `0.8418 → 0.8334`로 성능이 감소하였습니다.
    
14. Phonemes to Graphemes 처리

    허깅페이스에 올라와 있는 [kfkas/t5-large-korean-P2G](https://huggingface.co/kfkas/t5-large-korean-P2G) 모델을 사용하여 text에 사용된 Graphemes to Phoneme 노이즈를 제거했습니다. 노이즈를 전부 제거해 본 결과 기존 `0.8418 → 0.8407`로 감소하였습니다. 성능 하락의 원인을 학습 데이터뿐만 아니라 평가 데이터에도 동일한 노이즈가 있었기 때문으로 판단하였습니다. 
    
    학습 데이터의 원본 7,000개의 데이터를 그대로 남기고, 노이즈가 있는 row마다 노이즈가 제거된 결과를 추가로 넣어준 결과 `0.8418 → 0.8433`으로 성능이 향상되었습니다.
    
    학습 데이터와 평가 데이터의 노이즈 비율을 맞춰준다면 성능 향상이 있을 것으로 기대하여 노이즈를 450개가량 무작위로 drop 하여 실험해 보았지만, `0.8433 → 0.8317`로 성능이 감소하였습니다.

### Data Augmentation

1. AI Hub 뉴스 기사 기계독해 데이터
    
    AI Hub에 등록되어 있는 ‘뉴스 기사 기계독해 데이터’에서 추가로 약 12만 개의 데이터를 확보했습니다. 기존의 학습 데이터와 달리 추가로 분류된 `지역` 과 `기타` 를 제거해 준 후 약 75,000개의 데이터로 증강 했습니다. 추가된 데이터는 기존의 학습 데이터와 맞추기 위해 화살표, 온점, 말줄임표, 퍼센티지, 한국어, 영어, 한자를 제외한 다른 문장 부호는 제거했습니다.
    
    AI Hub 데이터 전체를 사용해 증강한 결과 F1 score가 대괄호가 존재하는 버전은 `0.8418 → 0.7920`, 대괄호가 존재하지 않는 버전은 `0.8418 → 0.7879`로 감소했습니다. 해당 실험을 통해 대괄호가 존재하는 것이 타당하다고 판단하였습니다.
    
    기존 학습 데이터의 분포를 따르기 위해 Uniform Distribution으로 증강해 약 3만 개의 데이터를 학습에 사용했고, 그 결과 대괄호가 없는 버전 기준 `0.7879 → 0.8040`으로 성능 향상이 있었습니다. 하지만 기존 0.8418에 비하면 성능 차이가 확연히 나기 때문에 AI Hub 증강은 폐기하였습니다.
    
2. Back Translation 
    
    네이버 파파고를 이용하여 한 → 영 → 한으로 역번역을 통한 증강을 시도했습니다. 1,617개를 증강하여 추가한 결과 `0.8394 → 0.8392`로 소폭 감소했습니다. 이후 hanspell을 적용한 결과 `0.8392 → 0.8395`로 성능 향상이 있었습니다.
    
    5,947개를 증강하여 추가한 결과는 `0.8394 → 0.8410`으로 상승한 결과를 볼 수 있었습니다. 동일하게 hanspell을 적용한 결과는 `0.8410 → 0.8392`로 성능이 하락하였습니다.
    
3. Easy Data Augmentation
    
    [EDA: Easy Data Augmentation Techniques for Boosting Performance on Text Classification Tasks] 논문 구현을 수정하여 학습 데이터에 적용하였습니다. 5,000개 이상의 데이터를 다룰 때는 전체 데이터의 10%를 증강하는 것이 성능 향상이 가장 크다는 논문 내용을 따라 데이터를 증강하여 7,000개의 데이터를 총 9,750개로 증강하였습니다.

## 🛠️**Requirements**
```
# 필요 라이브러리 설치
transformers==4.26.0
sentencepiece==0.1.96
numpy
pandas
pykospacing
evaluate==0.4.0
accelerate
scikit-learn
ipywidgets
protobuf==3.15.8
torch==1.11.0

```

## 최종 결과
- public: 9위, private: 5위
    
![스크린샷 2024-02-14 오전 3 08 36](https://github.com/boostcampaitech6/level2-nlp-datacentric-nlp-02/assets/80257041/5442311d-b108-401d-8d92-0577dd58055d)
![스크린샷 2024-02-14 오전 3 09 00](https://github.com/boostcampaitech6/level2-nlp-datacentric-nlp-02/assets/80257041/9d69265c-0b00-49ba-b355-6335f924ea1a)
