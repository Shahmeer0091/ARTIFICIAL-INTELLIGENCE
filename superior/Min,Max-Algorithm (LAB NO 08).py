def min_max(depth, is_maximizing, scores):
    if depth == 0 or not scores:
        return scores[-1]

    if is_maximizing:
        best_score = float('-inf')
        for score in scores:
            best_score = max(best_score, min_max(depth - 1, False, scores))
        return best_score
    else:
        best_score = float('inf')
        for score in scores:
            best_score = min(best_score, min_max(depth - 1, True, scores))
        return best_score


scores = [3, 5, 2, 9, 12, 4]
depth = 3
result = min_max(depth, True, scores)
print(f"The optimal score for the maximizing player is: {result}")
