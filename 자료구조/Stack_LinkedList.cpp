#include <iostream>

using namespace std;


struct Node {
	int data;
	Node* next;
};

Node* top = NULL;

void push(int data) {
	Node* node = new Node();
	node->data = data;
	node->next = top;
	top = node;
}

void Top() {
	if (top != NULL) {
		cout << top->data << endl;
	}
	else
		cout << "top is null\n";
}

void pop() {
	if (top == NULL) {
		cout << "stack is empty\n";
	}
	else {
		cout << top->data << endl;
		top = top->next;
	}
}

void print()
{
	Node* ptr;
	if (top == NULL) {
		cout << "stack is emtpy\n";
	}
	else {
		ptr = top;
		while (ptr != NULL) {
			cout << ptr->data << " ";
			ptr = ptr->next;
		}
	}
	cout << endl;
}

int main()
{
	print();
	Top();

	push(1);
	push(2);
	push(3);

	print();
	Top();
	pop();
	pop();

	print();
	Top();

	push(5);

	print();
	Top();

	return 0;
}
