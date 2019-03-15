typedef struct _S
{
	int a;
	char ch;
}S,*ps;

S s={10,'a'};
S sa[2]={{10,'a'},{20,'b'}};

int main(void)
{
	int i = 0;
	
	int a[10]={1,2,3,4,5,6,7,8,9,0};
	
	i++;
	++i;
	
	int a1 = i++;
	int a2 = ++i;
	
	if(i>10)
	{
		i -= 10;
	}
	else
	{
		i += 10;
	}
	
	int sum = 0;
	for(i = 0;i<10;i++)
	{
		sum += i;
	}
	
	i = 0;
	sum = 0;
	
	while(i<10)
	{
		sum += i;
		i++;
	}
	
	i = 0;
	sum = 0;
	
	do
	{
		sum += i;
		i++;
	}while(i<10);
	
	switch(i)
	{
		case 0:
			sum = 0;
			break;
		case 1:
			sum = 1;
			break;
		case 2:
			sum = 2;
			break;
		default:
			sum = -1;
			
	}
	
	s.a = 10;
	s.ch += 1;
	
	sum = 0;
	for(i=0;i<10;i++)
	{
			sum += a[i];
	}
	
	sum = 0;
	
	for(i = 0;i<2;i++)
	{
		sum += sa[i].a;
	}

	return 0;
}
