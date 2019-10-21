/*
 * Copyright (c) 2019 Gabriel B. Sant'Anna <baiocchi.gabriel@gmail.com>
 * @License Apache <https://gitlab.com/baioc/pygraphs>
 */

#ifndef STRUCTURES_PRIORITY_QUEUE_HPP
#define STRUCTURES_PRIORITY_QUEUE_HPP

#include <vector>
#include <tuple>
#include <functional> // less
#include <utility> // move, size_t
#include <algorithm> // swap, transform
#include <cassert>


namespace structures {

template <typename T, typename P = int, typename F = std::less<P>>
	// requires CopyConstructible<T>, MoveInsertable<T>, Comparable<T>,
	//          Comparable<P>
class PriorityQueue {
 public:
	PriorityQueue() = default;
	explicit PriorityQueue(int);

	bool empty() const;
	int size() const;

	void enqueue(T, P);
	T dequeue();
	const T& front() const;

	bool contains(const T&);
	std::vector<T> items() const;

 private:
	int parent(int);
	int children(int);
	void sift(int);
	void sink(int);
	static bool priorize(std::tuple<P,std::size_t,T>, std::tuple<P,std::size_t,T>);

	std::vector<std::tuple<P,std::size_t,T>> heap_;
	std::size_t count_{0};
};


template <typename T, typename P, typename F>
PriorityQueue<T,P,F>::PriorityQueue(int size)
{
	heap_.reserve(size);
}

template <typename T, typename P, typename F>
inline bool PriorityQueue<T,P,F>::empty() const
{
	return heap_.empty();
}

template <typename T, typename P, typename F>
inline int PriorityQueue<T,P,F>::size() const
{
	return heap_.size();
}

template <typename T, typename P, typename F>
inline bool PriorityQueue<T,P,F>::contains(const T& elem)
{
	for (const auto& entry: heap_)
		if (std::get<2>(entry) == elem) return true;

	return false;
}

template <typename T, typename P, typename F>
const T& PriorityQueue<T,P,F>::front() const
{
	assert(size() > 0);
	return std::get<2>(heap_[0]);
}

template <typename T, typename P, typename F>
inline int PriorityQueue<T,P,F>::parent(int child)
{
	return (child - 1) / 2;
}

template <typename T, typename P, typename F>
inline int PriorityQueue<T,P,F>::children(int parent)
{
	return 2*parent + 1;
}

template <typename T, typename P, typename Comp>
inline bool PriorityQueue<T,P,Comp>::priorize(
	std::tuple<P,std::size_t,T> lhs, std::tuple<P,std::size_t,T> rhs)
{
	// priority weights more, break tie via FIFO order
	return Comp()(std::get<0>(lhs), std::get<0>(rhs))
	       || (std::get<0>(lhs) == std::get<0>(rhs)
		       && std::get<1>(lhs) < std::get<1>(rhs));
}

template <typename T, typename P, typename F>
void PriorityQueue<T,P,F>::sift(int leaf)
{
	while (leaf > 0) {
		const int root = parent(leaf);
		if (priorize(heap_[leaf], heap_[root])) {
			std::swap(heap_[root], heap_[leaf]);
			leaf = root;
		} else {
			break;
		}
	}
}

template <typename T, typename P, typename F>
void PriorityQueue<T,P,F>::sink(int root)
{
	while (children(root) < size()) {
		int leaf = children(root);
		int swap = root;

		if (priorize(heap_[leaf], heap_[root]))
			swap = leaf;
		if (leaf+1 < size() && priorize(heap_[leaf+1], heap_[swap]))
			swap = leaf + 1;
		if (swap == root)
			break;

		std::swap(heap_[root], heap_[swap]);
		root = swap;
	}
}

template <typename T, typename P, typename F>
void PriorityQueue<T,P,F>::enqueue(T elem, P prio)
{
	auto entry = std::make_tuple(prio, count_++, std::move(elem));
	heap_.emplace_back(std::move(entry));
	sift(size() - 1);
}

template <typename T, typename P, typename F>
T PriorityQueue<T,P,F>::dequeue()
{
	assert(size() > 0);
	auto top = std::get<2>(heap_[0]);
	std::swap(heap_[0], heap_[size() - 1]);
	heap_.pop_back();
	sink(0);
	return top;
}

template <typename T, typename P, typename F>
std::vector<T> PriorityQueue<T,P,F>::items() const
{
	std::vector<T> vec(heap_.size());
	std::transform(
		heap_.begin(), heap_.end(),
		vec.begin(),
		[](auto tup){ return std::get<2>(tup); }
	);
	return vec;
}

} // namespace structures

#endif // STRUCTURES_PRIORITY_QUEUE_HPP
