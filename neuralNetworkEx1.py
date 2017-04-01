#신경망 클래스의 정의
class neuralNetwork:

    #신경망 초기화하기 
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):

        #입력, 은닉, 출력 계층의 노드 개수 설정
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes

        #학습률
        self.learning_rate = learning_rate
    
    #신경망 학습시키기
    def train(self):
        pass
    
    #신경망에 질의하기
    def query(self):
        pass


def main():
    #입력, 은닉, 출력 노드의 수
    input_nodes = 3
    hidden_nodes = 3
    output_nodes = 3

    #학습률은 0.3으로 정의
    learning_rate = 0.3

    #신경망의 인스턴스를 생성
    n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
    pass

if __name__ == "__main__":
    main()