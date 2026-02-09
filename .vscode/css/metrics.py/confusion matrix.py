def main():
    TP = 50
    TN = 40
    FP = 10
    FN = 5

    accuracy = (TP + TN) / (TP + TN + FP + FN)
    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    f1_score = 2 * precision * recall / (precision + recall)

    print("Confusion Matrix")
    print("TP =", TP, "FP =", FP)
    print("FN =", FN, "TN =", TN)

    print("\nPerformance Metrics")
    print("Accuracy :", accuracy)
    print("Precision:", precision)
    print("Recall   :", recall)
    print("F1 Score :", f1_score)

if __name__ == "__main__":
    main()
