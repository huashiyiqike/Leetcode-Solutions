class PeekingIterator implements Iterator<Integer> {
    Integer peek;
   Iterator<Integer> iter;
	public PeekingIterator(Iterator<Integer> iterator) {
	    // initialize any member here.
	   iter = iterator;
	   peek = iter.hasNext()?iter.next():null;
	    
	}

    // Returns the next element in the iteration without advancing the iterator.
	public Integer peek() {
        return peek;
	}

	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.m

	@Override
	public Integer next() {
	    if(peek == null){
	       throw new java.util.NoSuchElementException();
	    }
	    Integer value = peek;
	    peek = iter.hasNext()?iter.next():null;
	    return value;
	}

	@Override
	public boolean hasNext() {
	    if(peek != null){
	        return true;
	    }else{
	        return false;
	    }
	}
}