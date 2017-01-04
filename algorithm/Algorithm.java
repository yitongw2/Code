package Algorithm;

public class Algorithm
{

	public static void main(String[] args)
	{
		int r;
		for (int i=1;i<11;++i)
		{
			for (int j=1;j<11;++j)
			{
				r=ksb_multi(i,j);
				if (r!=i*j)
					System.out.println("Error "+i+"*"+j+"="+r+"="+i*j);
			}
		}

	}
	
	public static int ksb_multi(int I, int J)
	{
		/* the idea is to separate an int I of n digits to two parts: low-order bits and high-order bits 
		 * so that each part has n/2 digits.
		 * I = (high-order part)*(base^(digits/2)) + (low-order part)
		 * 
		 * example (I=14, base=10, digits=2):
		 * 	I = 1*(10^(2/2)) + 4 = 14
		 * 
		 * assume I and J are represented in base 2
		 * I=Ih*(2^(k/2))+Il
		 * J=Jh*(2^(k/2))+Jl
		 * 
		 * then,
		 * I*J=Ih*Jh*(2^k)+Ih*Jl*(2^(k/2))+Il*Jh*(2^(k/2))+Il*Jl
		 * 
		 * Analysis:
		 * 	- addition takes O(n) time
		 *  - 4 recursive multiplications to compute:
		 *  	* Ih*Jh
		 *  	* Ih*Jl
		 *  	* Il*Jh
		 *  	* Il*Jl
		 *  - each multiplication takes input of k/2 digits (asssume I has k digits)
		 * 	- formula: T(n)=4T(n/2)+O(n)
		 * 				...
		 * 				by master theorem, T(n)=O(n^2)
		 * 
		 * 	Magic trick:
		 * 		Ih*Jl+Il*Jh = (Ih+Il)*(Jh+Jl)-Ih*Jh-Il*Jl 
		 * 		assume we know the result of Ih*Jh and Il*Jl (turns out we have to compute them anyway), 
		 * 		we only need to perform one more multiplication (Ih+Il)*(Jh+Jl).
		 * 		
		 * 		then, 
		 * 		I*J=Ih*Jh*(2^k)+[(Ih+Il)*(Jh+Jl)-Ih*Jh-Il*Jl]*(2^(k/2))+Il*Jl
		 * 
		 * 		therefore, 
		 * 		T(n)=3T(n/2)+O(n)
		 * 		...	
		 * 		by master theorem, T(n)=O(n^log3)
		 * 
		 */
		
		// determines how many digits are there 
		int len=Math.max(Integer.toBinaryString(I).length(), Integer.toBinaryString(J).length());
		// base case (could vary depending on requirements)
		if (len==1)
			return I*J;
		int highOrder, Ih, Il, Jh, Jl, p, q, r;
		// calculate how many positions we need to shift right in order to obtain high-order bits
		highOrder=(int)Math.ceil(len/2.0);
		// shifting right by the number of positions specified by highOrder
		Ih=I>>highOrder;
		Jh=J>>highOrder;
		// in order to obtain low-order bits, we need to create a mask. 
		// the mask here is a special collection of bits where the high-order bits are all 0 and the low-order bits are all 1
		// then bitwise and operator will erase the high-order bits of the int and keep the lower-order bits intact.
		Il=I&((1<<highOrder)-1);
		Jl=J&((1<<highOrder)-1);
		// recursively compute Ih*Jh, Il*Jl and (Ih+Il)*(Jh+Jl)
		p=ksb_multi(Ih, Jh);
		q=ksb_multi(Il, Jl);
		r=ksb_multi(Ih+Il, Jh+Jl)-p-q;
		// shift positions back 
		return (p<<(highOrder*2))+q+(r<<highOrder);
	}

}
