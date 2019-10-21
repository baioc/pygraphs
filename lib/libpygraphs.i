// SWIG interface definition
%module libpygraphs
%{
	// preprocessor directives directly included into wrapper code
	#include "graph.hpp"
	#include "priority_queue.hpp"
%}

// wrap standard headers
%include "std_string.i"
%include "std_unordered_map.i"
%include "std_vector.i"

// ignores
//

// parse files to generate wrappers
%include "graph.hpp"
%include "priority_queue.hpp"

// explicit template instantiation
%template(Graph) structures::Graph<std::string,double>;
%template(Digraph) structures::Graph<std::string,double,true>;
%template(GraphEdges) std::unordered_map<std::string,double>;
%template(GraphNodes) std::unordered_map<std::string,std::unordered_map<std::string,double>>;
%template(PrioQ) structures::PriorityQueue<std::string, float>;
%template(Labels) std::vector<std::string>;

// type mapping
//
