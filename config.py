class Config:
    def __init__(self):
        # Model configurations
        self.model_type = "BERT"  # Choose between "BERT" or "GPT-2"
        self.bert_model_name = "bert-base-uncased"  # Pretrained BERT model name
        self.gpt2_model_name = "gpt2"  # Pretrained GPT-2 model name
        self.max_sequence_length = 128  # Maximum sequence length for input data
        self.batch_size = 32  # Batch size for training

        # Training configurations
        self.learning_rate = 1e-4
        self.num_epochs = 5
        self.train_data_path = "data/training_data.txt"  # Path to training data
        self.test_data_path = "data/testing_data.txt"  # Path to testing data

        # Evaluation configurations
        self.eval_metrics = ["accuracy", "precision", "recall", "f1_score"]  # Evaluation metrics to compute
