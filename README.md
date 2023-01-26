# msa-with-genetic-algorithm
유전 알고리즘을 활용한 다중 서열 정리

## 개요 
본 프로그램은 바이오인포매틱스 분야의 핵심 주제인 **multiple sequence alignment**를 수행하기 위해 개발되었다.  
다양한 msa 수행 알고리즘 중에서도, genetic algorithm을 이용한 최적화 기법을 대상으로 하였다.

<br>

## 알고리즘 
본 프로그램의 알고리즘 모식도는 다음과 같다.  
> <img src="https://user-images.githubusercontent.com/45115733/214784959-f15d8db2-5531-4202-bfb0-12e900cdc469.png" width="40%" height="30%"/>

+ **Initialize** --> multiple sequence로 부터 초기 정렬 모집단 형성
+ **Evaluation** --> 모집단으로부터 교체비용 + 갭비용 계산
+ **Breeding** --> 평가값을 기준으로 부모 선정 및 교배 진행
+ **Generation** --> 새로운 자식 세대 형성 및 전이  

구체적인 사항은 [presentation.pdf](https://github.com/82KJ/msa-with-genetic-algorithm/blob/main/presentation.pdf)를 참고해주세요.

<br>

## 결과
CLUSTWAL W 기법과 직접적인 평가값 비교 진행
|Chromosome|SAGA 평균|SAGA 최대값|CLUSTWALW|
|:---:|:---:|:---:|:---:|
|100|966.5|1085.0|1856.5|
|200|1151|1233.5|1856.6|
|300|1250|1631.5|1856.5|
|400|1246.8|1457.5|1856.5|

전반적으로 CLUSTWALW기법보다 **낮은 결과치**를 보임.  
<br>
구체적인 결과 분석은 [presentation.pdf](https://github.com/82KJ/msa-with-genetic-algorithm/blob/main/presentation.pdf)를 참고해주세요.

<br>

## 참고 자료
- [진화 알고리즘을 사용한 복수 염기서열 정렬](https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=JAKO199911919923925) [미생물학회지 v.35 no.2, 1999년]
- [SAGA: Sequence Alignment by Genetic Algorithm](https://academic.oup.com/nar/article/24/8/1515/2359898) [Nucleic Acids Research, v.24, no.8, 1996년]



