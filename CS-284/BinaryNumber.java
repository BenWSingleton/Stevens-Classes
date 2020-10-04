import java.util.*;

//Benjamin Singleton
//I pledge my honor that I have abided by the Stevens Honor System

public class BinaryNumber {
	
	private int data[];
	private int length;
	
	public BinaryNumber(int length)
	{
		data = new int[length];
	}
	
	public BinaryNumber(String str)
	{
		length = str.length();
		data = new int[length];
		for (int i=0; i<str.length(); i++) {
			int pos=0;
			pos=str.charAt(i);
			int val;
			val=Character.getNumericValue(pos);
			data[i] = val;
		}
	}
	
	public int getLength() {
		return data.length;
	}
	
	public int getDigit(int index) throws Exception {
		if (index<0) {
			throw new Exception("Input must be 0 or greater");
		}
		return data[index];
	}
	
	public int[] getInnerArray() {
		return data;
	}

	public void prepend(int amount) throws Exception {
		if (amount<0) {
			throw new Exception("Amount bust be greater than zero");
		}
		int leng=amount+length;
		int dataTemp[] = new int[amount+length];
			
		for(int i=amount; i<leng; i++) {
			dataTemp[i]=data[i-amount];
		}
			
		data=dataTemp;
		length=dataTemp.length;
		
	}
	
	public static int[] bwor(BinaryNumber bn1, BinaryNumber bn2) throws Exception {
		if (bn1.getLength()>bn2.getLength()) {
			bn2.prepend(bn1.getLength()-bn2.getLength());
		}
		if (bn1.getLength()<bn2.getLength()) {
			bn1.prepend(bn2.getLength()-bn1.getLength());
		}
		
		int bworbin[];
		bworbin = new int[bn1.getLength()];
		
		for (int i=bn1.getLength()-1; i>=0; i--) {
			if (bn1.getDigit(i)==1 || bn2.getDigit(i)==1) {
				bworbin[i]=1;
			}
			else {
				bworbin[i]=0;
			}
		}
		return bworbin;
	}
	
	public static int[] bwand(BinaryNumber bn1, BinaryNumber bn2) throws Exception {
		if (bn1.getLength()>bn2.getLength()) {
			bn2.prepend(bn1.getLength()-bn2.getLength());
		}
		if (bn1.getLength()<bn2.getLength()) {
			bn1.prepend(bn2.getLength()-bn1.getLength());
		}
		
		int bwandbin[];
		bwandbin = new int[bn1.getLength()];
		
		for (int i=bn1.getLength()-1; i>=0; i--) {
			if (bn1.getDigit(i)==1 && bn2.getDigit(i)==1) {
				bwandbin[i]=1;
			}
			else {
				bwandbin[i]=0;
			}
		}
		return bwandbin;
	}
	
	void bitShift(int direction, int amount) throws Exception {
		
		if (amount>length && (direction!=1 || direction!=-1)) {
			throw new Exception("Invalid Input");
		}
		
		if (direction==1) {
			int dataTemp[] = new int[length-amount];
			for (int i=amount; i<length; i++) {
				dataTemp[i-amount]=data[i];
			}
			data=dataTemp;
			length=dataTemp.length;
		} else {
			int dataTemp[] = new int[length+amount];
			for (int i=0; i<length; i++) {
				dataTemp[i]=data[i];
			}
			data=dataTemp;
			length=dataTemp.length;
		}
	}
	
	public void add(BinaryNumber aBinaryNumber) throws Exception {
		if (data.length>aBinaryNumber.getLength()) {
			aBinaryNumber.prepend(data.length-aBinaryNumber.getLength());
		}
		if (data.length<aBinaryNumber.getLength() ) {
			int diff = aBinaryNumber.getLength()-length;
			int dataTemp[] = new int[aBinaryNumber.getLength()];
				
			for(int i=diff; i<aBinaryNumber.getLength(); i++) {
				dataTemp[i]=data[i-diff];
			}
				
			data=dataTemp;
			length=dataTemp.length;
		}
		
		String answer="";
		int carry=0;
		for (int i=length-1; i>=0; i--) {
			if (aBinaryNumber.getDigit(i)==0 && data[i]==0 && carry==0) {
				answer+="0";
				carry=0;
			}
			else if (aBinaryNumber.getDigit(i)==0 && data[i]==0 && carry==1) {
				answer+="1";
				carry=0;
			}
			else if (aBinaryNumber.getDigit(i)==0 && data[i]==1 && carry==0) {
				answer+="1";
				carry=0;
			}
			else if (aBinaryNumber.getDigit(i)==0 && data[i]==1 && carry==1) {
				answer+="0";
				carry=1;
			}
			else if (aBinaryNumber.getDigit(i)==1 && data[i]==0 && carry==0) {
				answer+="1";
				carry=0;
			}
			else if (aBinaryNumber.getDigit(i)==1 && data[i]==0 && carry==1) {
				answer+="0";
				carry=1;
			}
			else if (aBinaryNumber.getDigit(i)==1 && data[i]==1 && carry==0) {
				answer+="0";
				carry=1;
			}
			else {
				answer+="1";
				carry=1;
			}
		}
		if (carry==1) {
			answer+="1";
		}
		
		String revanswer="";
		for (int i = answer.length() - 1; i >= 0; i--) {
	        revanswer = revanswer + answer.charAt(i);
	    }
		
		int dataTemp[] = new int[answer.length()];
		
		for (int i=0; i<answer.length(); i++) {
			dataTemp[i]=Character.getNumericValue(revanswer.charAt(i));
		}
		
		data=dataTemp;
		length=dataTemp.length;
	}
	
	public String toString() {
		String value="";
		for (int i=0; i<data.length; i++) {
			value+=String.valueOf(data[i]);
		}
		return value;
	}
	
	public int toDecimal() {
		int answer = 0;
		
		for (int i = length -1; i >=0; i--) {
			answer += data[length - i -1] * Math.pow(2, i);
		}
		
		return answer;
	}
}
