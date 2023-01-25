import evaluation
from evaluation import evaluation_func
from selection import selection
from initpop import init_pop
from crossover import crossover
from mutation import mutation


# txt 파일에서 sequence들 가져오기
lines = evaluation.read_input_lines("data\\sequences\\data_1.txt")
# 각 sequence 길이 맞추기 ('-' 삽입) 
lines = evaluation.fill_diff(lines)
# line 들에는 평가값을 구하려는 sequence들의 배열이 들어 있다.

# 반복을 위한 변수 정의
chromosomes = 100 # 한 세대의 데이터 수
generations = 10 # 최대 반복 수
min_generations = 200 # 최소 반복 수

# 반복 횟수를 측정하기 위한 변수
generation = 0
# 세대 별 최대 평가값 저장하기 위한 변수
best_evaluation = []

# 초기 세대 생성
# 한 데이터의 구조
# sequence : [배열], evaluation : 평가값
pop = init_pop(lines, chromosomes) #population 0



while (generation < generations):
    print(generation)
    # 최대값이 저장되기 위해 가장 낮은 값 설정
    max_value = -9999
    # 세대의 데이터들에 대한 evaluation 측정
    for x in range(len(pop)):
        #  각 데이터에 대한 evalution 계산
        pop[x]["evaluation"] = evaluation_func(pop[x]["sequence"])

        # 각 세대의 최대 평가값을 저장하기 위한 부분
        if(max_value <pop[x]["evaluation"]):
            max_value = pop[x]["evaluation"]
    # 현재 세대 최대 평가값 저장
    best_evaluation.append(max_value)

    # crossover를 통하여 새롭게 생성한 데이터들이 저장될 배열
    new_pop = []

    # 전체 생성된 데이터 수 만큼 세로운 데이터 생성
    for x in range(chromosomes):
        # 현제 세대에서 특정 데이터 2개 선정
        p1, p2 = selection(pop)
        # 두 데이터를 crossover하여 새로운 데이터 생성 
        data = crossover(p1["sequence"], p2["sequence"])
        data = mutation(data)

        # 서로 다른 길이의 sequence를 crossover하여 이후 evalution에 문제 발생 가능
        # 따라서 길이를 맞춰주는 과정을 추가해야 한다.
        data = evaluation.fill_diff(data) # 길이 맞추기
        data = evaluation.remove_diff(data) # gap만 있는 열 없애기

        # new pop에 생성한 데이터 추가
        new_pop.append({"sequence": data, "evaluation": 0})

        
    # 새로운 데이터에 대한 evaluation 계산
    for x in range(len(new_pop)):
        new_pop[x]["evaluation"] = evaluation_func(new_pop[x]["sequence"])

    # 각 population 들을 evalution 순으로 정렬한다. 
    # reverse를 적용하여 큰 순으로 정렬된다. ( pop[0]: 큰 값 -> pop[chrom-1]: 작은 값)
    pop = sorted(pop, key=lambda pop: pop["evaluation"], reverse=True)
    new_pop = sorted(new_pop, key=lambda new_pop: new_pop["evaluation"], reverse= True)

    # pop을 50% new_pop을 50% 비율로 섞는다.
    for x in range(int(len(pop)/2)): # population 크기의 반 만큼 반복
        # pop의 마지막 데이터(evalution이 가장 작은 데이터)를 제거
        pop.pop() 
        # pop의 처음 데이터로 new pop의 데이터 추가
        # x는 0 ~ 전체 데이터의 반 만큼 반복 되므로 new pop의 evaluation이 가장 큰 값들만 추가된다.
        pop.insert(0, new_pop[x]) 


    # 한 세대 증가
    generation += 1

print(best_evaluation)

pop = sorted(pop, key=lambda pop: pop["evaluation"], reverse=True)
print(pop[0]["sequence"])
print(pop[0]["evaluation"])
