import config
import utils.evaluation as evaluation
from model.bert import BERTModel
from model.gpt2 import GPT2Model

def main():
    # Load configuration
    cfg = config.Config()

    # Load test data
    with open(cfg.test_data_path, 'r') as file:
        test_data = file.readlines()
    test_data = [line.strip() for line in test_data]

    # Load pretrained model
    if cfg.model_type == "BERT":
        model = BERTModel(cfg)
        model.load_pretrained_weights(cfg.bert_model_name)
    elif cfg.model_type == "GPT-2":
        model = GPT2Model(cfg)
        model.load_pretrained_weights(cfg.gpt2_model_name)

    # Fine-tune model (if needed)
    # model.fine_tune(training_data)

    # Perform predictions on test data
    predicted_labels = model.predict(test_data)

    # True labels (if available)
    true_labels = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]  # Example true labels, replace with actual labels if available

    # Evaluate model performance
    accuracy = evaluation.calculate_accuracy(true_labels, predicted_labels)
    precision = evaluation.calculate_precision(true_labels, predicted_labels)
    recall = evaluation.calculate_recall(true_labels, predicted_labels)
    f1_score = evaluation.calculate_f1_score(true_labels, predicted_labels)

    # Print evaluation results
    print("Evaluation Results:")
    print("Accuracy:", accuracy)
    print("Precision:", precision)
    print("Recall:", recall)
    print("F1 Score:", f1_score)

if __name__ == "__main__":
    main()
