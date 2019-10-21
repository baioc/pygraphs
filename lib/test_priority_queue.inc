#include <catch2/catch.hpp>

#include "priority_queue.hpp"
using structures::PriorityQueue;

#include <functional> // greater


TEST_CASE("PriorityQueues maintain their elements sorted by lowest priority (default)", "[PriorityQueue]")
{
	PriorityQueue<char> q;
	REQUIRE(q.empty());
	REQUIRE(q.size() == 0);

	REQUIRE(!q.contains('c'));
	q.enqueue('c', 5);
	REQUIRE(q.contains('c'));
	REQUIRE(q.size() == 1);

	REQUIRE(!q.contains('p'));
	q.enqueue('p', 7);
	REQUIRE(q.contains('p'));
	REQUIRE(q.size() == 2);

	REQUIRE(!q.contains('z'));
	q.enqueue('z', 1);
	REQUIRE(q.contains('z'));
	REQUIRE(q.size() == 3);

	REQUIRE(!q.contains('s'));
	q.enqueue('s', 1);
	REQUIRE(q.contains('s'));
	REQUIRE(q.size() == 4);

	REQUIRE(!q.contains('t'));
	q.enqueue('t', 3);
	REQUIRE(q.contains('t'));
	REQUIRE(q.size() == 5);

	REQUIRE(q.dequeue() == 'z');
	REQUIRE(q.size() == 4);

	REQUIRE(q.dequeue() == 's');
	REQUIRE(q.size() == 3);

	REQUIRE(q.dequeue() == 't');
	REQUIRE(q.size() == 2);

	REQUIRE(q.dequeue() == 'c');
	REQUIRE(q.size() == 1);

	REQUIRE(q.dequeue() == 'p');
	REQUIRE(q.size() == 0);
}


TEST_CASE("PriorityQueues are templated to any sorting order", "[PriorityQueue][template]")
{
	PriorityQueue<char,int,std::greater<int>> q;

	q.enqueue('c', 5);
	q.enqueue('p', 7);
	q.enqueue('z', 1);
	q.enqueue('s', 1);
	q.enqueue('t', 3);

	REQUIRE(q.dequeue() == 'p');
	REQUIRE(q.dequeue() == 'c');
	REQUIRE(q.dequeue() == 't');
	REQUIRE(q.dequeue() == 'z');
	REQUIRE(q.dequeue() == 's');
}

TEMPLATE_TEST_CASE(
	"PriorityQueues return ordered iterables", "[PriorityQueue]",
	char, short, int, long, long long, float, double, long double
) {
	PriorityQueue<TestType, TestType> q;

	q.enqueue(0, 0);
	q.enqueue(1, 1);
	q.enqueue(2, 2);
	q.enqueue(3, 3);
	q.enqueue(4, 4);

	for (auto it = q.items().begin(); it < q.items().end(); it++)
		if (it + 1 != q.items().end()) REQUIRE(*it <= *(it + 1));
}