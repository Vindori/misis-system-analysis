import numpy as np

def compute_tau_kendall(expert_rankings):
    ranking_matrix = np.zeros((len(expert_rankings[0]), len(expert_rankings)))
    eta_matrix = np.array([np.full(len(expert_rankings), len(expert_rankings[0]) - i) for i in range(len(expert_rankings[0]))])
    sorted_items = sorted(expert_rankings[0])

    for idx_expert, rankings in enumerate(expert_rankings):
        for idx_item, item in enumerate(sorted_items):
            ranking_matrix[idx_item, idx_expert] = len(rankings) - rankings.index(item)

    var_eta = np.sum((np.sum(eta_matrix, axis=1) - np.mean(np.sum(eta_matrix, axis=1)))**2) / (len(expert_rankings[0]) - 1)
    var_rankings = np.sum((np.sum(ranking_matrix, axis=1) - np.mean(np.sum(ranking_matrix, axis=1)))**2) / (len(expert_rankings[0]) - 1)

    print(var_rankings)
    print(var_eta)

    return var_rankings / var_eta

def task():
    ExpertA = ["O1", "O2", "O3"]
    ExpertB = ["O1", "O3", "O2"]
    ExpertC = ["O1", "O3", "O2"]

    views_experts = [ExpertA, ExpertB, ExpertC]

    tau_result = compute_tau_kendall(views_experts)
    return tau_result

if __name__ == "__main__":
    task()