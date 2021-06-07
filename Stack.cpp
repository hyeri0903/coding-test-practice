#include <iostream>

using namespace std;

typedef struct Stack
{
	int top;
	int maxsize;
	int *arr;

	Stack(int size);
	~Stack();
	bool isFull(), isEmpty();
	void push(int n);
	int pop();
	void print();
};

Stack::Stack(int size) {
	maxsize = size;
	top = -1;
	arr = new int[maxsize];
}

Stack::~Stack() {
	delete[] arr;
}

bool Stack::isFull() {
	if (top == maxsize - 1)
		return true;
	else
		return false;
}

bool Stack::isEmpty() {
	if (top == -1)
		return true;
	else
		return false;
}

void Stack::push(int n) {
	if (!isFull()) {
		arr[++top] = n;
	}
	else {
		cout << "Full!" << endl;
	}
}

int Stack::pop() {
	if (!isEmpty()) {
		return arr[top--];
	}
	else {
		cout << "Empty!" << endl;
	}
}

void Stack::print() {
	for (int i = 0; i < top + 1; i++) {
		cout << arr[i] << endl;
	}
}


int main()
{
	Stack arr(10);
	arr.push(1);
	arr.push(4);
	arr.push(10);

	arr.pop();
	arr.push(6);

	arr.print();

	return 0;
}
