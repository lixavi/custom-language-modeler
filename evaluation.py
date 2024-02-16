from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def calculate_accuracy(true_labels, predicted_labels):
    """
    Calculate accuracy of the language model predictions.
    """
    accuracy = accuracy_score(true_labels, predicted_labels)
    return accuracy

def calculate_precision(true_labels, predicted_labels):
    """
    Calculate precision of the language model predictions.
    """
    precision = precision_score(true_labels, predicted_labels, average='weighted')
    return precision

def calculate_recall(true_labels, predicted_labels):
    """
    Calculate recall of the language model predictions.
    """
    recall = recall_score(true_labels, predicted_labels, average='weighted')
    return recall

def calculate_f1_score(true_labels, predicted_labels):
    """
    Calculate F1 score of the language model predictions.
    """
    f1 = f1_score(true_labels, predicted_labels, average='weighted')
    return f1
 
