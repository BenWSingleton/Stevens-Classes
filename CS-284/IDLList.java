//Benjamin Singleton
//I pledge my honor that I have abided by the Stevens Honor System.

import java.util.ArrayList;

public class IDLList<E>
{
	private static class Node<E> {
		private E data;
		private Node<E> next = null;
		private Node<E> prev = null;
		
		public Node(E elem) {
			this.data=elem;
			next=null;
			prev=null;
		}
		
		public Node(E elem, Node<E> prev, Node<E> next) {
			this.data=elem;
			this.prev=prev;
			this.next=next;
		}
	}
	
	private Node<E> head = null;
	private Node<E> tail = null;
	private int size = 0;
	private ArrayList<Node> indices;
	
	public IDLList() {
		head=null;
		tail=null;
		indices = null;
		size=0;
	}

	//Adds node at Index
	public boolean add(int index, E elem) throws Exception {
		if (index < 0 || index > size) {
			throw new Exception("Invalid index");
		}
		Node<E> newNode = new Node<E>(elem);				
		Node<E> current = head;
		
		for (int i = 1; i < index; i++) {
			current = current.next;
		}
		
		newNode.next = current.next;
		current.next = newNode;
		newNode.prev = current;
		newNode.next.prev = newNode;
		
		size++;
		return true;
	}

	//Adds Node at head
	public boolean add(E elem) {
		Node<E> newNode = new Node<E>(elem);
		
		if (head == null) {		
			head = newNode;
			tail = newNode;
		} else {			
			newNode.next = head;
			head.prev = newNode;
			head = newNode;
		}
		size++;
		return true;
	}
	
	//Adds Node at tail
	public boolean append(E elem) {
		Node<E> newNode = new Node<E>(elem);
		newNode.prev = tail;
		tail.next = newNode;
		tail = newNode;
		size++;
		return true;
	}
	
	//Gets element at index
	public E get(int index) throws Exception {
		if (index < 0 || index > size-1) {
			throw new Exception("Invalid Index");
		}
		Node<E> current = head;
		int count=0;
		while (current != null) {
			if (count == index) {
				return current.data; 
			} else {
				count++;
				current = current.next;
			}
		}
		return null;
	}
	
	//Returns element at head
	public E getHead() {
		return head.data;
	}
	
	//Returns element at tail
	public E getLast() {
		return tail.data;
	}
	
	//Returns size
	public int size() {
		return size;
	}

	//Removes node at head 
	public E remove() throws Exception {
		this.removeAt(0);
		return this.getHead();
	}

	public E removeLast() throws Exception {
		this.removeAt(size);
		return this.getLast();
	}

	//Removes element at index
	public E removeAt(int index) throws Exception {
		if (index < 0 || index > size) {
			throw new IllegalStateException("Invalid Input");
		}
		Node<E> current = head;
		for (int i=1; current != null && i < index; i++) {
			current = current.next;
		}
		
		if (head == current) {
			head = current.next;
		}
		
		if (current.next != null) {
			current.next.prev = current.prev;
		}
		
		if (current.prev != null) {
			current.prev.next = current.next;
		}
		size--;
		return current.data;
	}

	//Removes first occurrence of element in list
	public boolean remove(E elem) throws Exception {
		  Node<E> current = head;
		  for (int i = 0; i < size; i++) {
				if (current.data == elem) {
					this.removeAt(i+1);
					return true;
				} else {
					current = current.next;
				}
		  }
		  return false;
	}

	//Returns string representation of the linked list
	public String toString() {
		StringBuilder sb = new StringBuilder("[");
		Node<E> p = head;
		if (p != null) {
			while (p.next != null) {
				sb.append(p.data.toString());
				sb.append(" ==> ");
				p = p.next;
			}
			sb.append(p.data.toString());
		}
		sb.append("]");
		return sb.toString();
	}
}
