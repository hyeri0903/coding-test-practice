#include <iostream>

using namespace std;

struct Queue {
	int front;
	int rear;
	int maxsize;
	int *arr;

	Queue(int size);
	~Queue();
	void push(int n);
	void pop();
	bool isFull();
	bool isEmpty();
	void print();
	int returnFront();
	int returnBack();
};

Queue::Queue(int size) {
	front = -1;
	rear = -1;
	maxsize = size;
	arr = new int[size];
	
}

Queue::~Queue() {
	delete[] arr;
}

bool Queue::isFull() {
	if ( (rear+1)%maxsize == front) {
		return true;
	}
	else
		return false;
}

bool Queue::isEmpty() {
	if (rear == front)
		return true;
	else
		return false;
}

void Queue::push(int n) {
	if (!isFull()) {
		rear = (rear + 1) % maxsize;
		arr[rear] = n;
	}
	else {
		cout << "Full!" << endl;
	}
}

void Queue::pop() {
	if (!isEmpty()) {
		front = (front + 1) % maxsize;
	}
	else {
		cout << "Empty!!" << endl;
	}
}

void Queue::print() {
	for (int i = front; i < rear + 1; i++) {
		cout << arr[i] << " ";
	}
}

int Queue::returnFront() {
	return arr[(front + 1) % maxsize];
}
int Queue::returnBack() {
	return arr[rear];
}

int main()
{
	Queue arr(10);
	arr.push(1);
	arr.push(2);
	arr.push(3);
	
	arr.pop();
	arr.push(4);

	while (!arr.isEmpty()) {
		cout << arr.returnFront() << " ";
		arr.pop();
	}

	return 0;
}
