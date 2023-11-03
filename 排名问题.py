# 朗
# 开发时间：2023
path = 'data/data22463/成绩单.txt'
with open(path, 'r') as file:

    def read_scores(path):
        scores = {}
        with open(path, 'r') as file:
            for line in file:
                 parts = line.strip().split()
                 name = parts[0]
                 score1 = int(parts[1])
                 score2 = int(parts[2])
                 score3 = int(parts[3])
                 total_score = score1 + score2 + score3
                 scores[name] = total_score
        return scores

def write_total_scores(path, scores):
    ranking = sorted(scores.items(), key=lambda x: x[1], reverse=True)#匿名函数
    with open(path, 'w') as file:
        rank = 1
        prev_score = None
        for name, score in ranking:
            if prev_score is None or score != prev_score:
                file.write("排名: {}    ".format(rank))
            else:
                file.write("并列排名: {}    ".format(rank))
            file.write("{}    {}\n".format(name, score))
            rank += 1
            prev_score = score

def search_score(name, scores):
    for i, (student, score) in enumerate(scores.items(), 1):
        if student == name:
            return score, i
    return None, None

scores = read_scores("scores.txt")
write_total_scores("total_scores.txt", scores)

while True:
    query_name = input("请输入学生姓名：")
    score, rank = search_score(query_name, scores)
    if score is None:
        print("未找到该学生")
    else:
        print("总分: {}, 排名: {}".format(score, rank))
