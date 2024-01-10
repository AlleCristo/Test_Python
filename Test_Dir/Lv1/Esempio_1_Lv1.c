#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define MAXLEN 250

int main()
{
		
	char s[MAXLEN];
	char c;
	int count = 0;
	
	printf("\nInserisci una stringa di massimo %d caratteri (la stringa si intende priva di spazi)--> ", MAXLEN);
	scanf("%s", s);
	
	while(getchar() != '\n');
	
	printf("\nInserisci il carattere da ricercare --> ");
	scanf("%c", &c);
	
	while(getchar() != '\n');
	
	printf("\nCerco il numero di occorrenze del carattere %c nella stringa \"%s\" \n", c, s);
	
	int i;
	for(i = 0; i < strlen(s); i++)
	{
		if(s[i] == c)
		{
			count++;
		}
	}
	
	printf("\n-- Nella stringa \"%s\" sono state trovate %d occorrenze del carattere %c\n", s, count, c);
	
	
	
	return 0;
}
