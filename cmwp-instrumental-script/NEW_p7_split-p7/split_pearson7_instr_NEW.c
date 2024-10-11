#include <stdio.h>
#include <stdlib.h>
#include <math.h>

main(int argc, char *argv[])
{
double k,dk,k_edge, p,fw, left_shape, right_shape, left_hwhm, right_hwhm, stepsize;
double k_filenev;
char *filenev;
FILE *profile;
long int i, i_max;

filenev=(char*)calloc(1024,sizeof(char));

//itt ellenorzi, hogy megvan-e az osszes argumentum
if (argv[1] == NULL || argv[2] == NULL || argv[3] == NULL || argv[4] == NULL || argv[5] == NULL || argv[6] == NULL || argv[7] == NULL) {printf("\n\nUsage: ./program_name peak_position left_hwhm right_hwhm left_shape right_shape number_of_datapoints MAX_value_of_deltaK\n\n"); exit(-42);}
else;

if (k_edge <=0 ) {printf("\nMAX_value_of_deltaK must be non-zero and positive!\n"); exit(-42);}
else;

k_filenev = atof(argv[1]);

left_hwhm = atof(argv[2]);

right_hwhm = atof(argv[3]);

left_shape = atof(argv[4]);

right_shape = atof(argv[5]);

i_max = atof(argv[6]);

k_edge = atof(argv[7]);

//ez roviditi le a szamot egy 4 karakter hosszusagu filenevve
gcvt(k_filenev,4,filenev);


profile=fopen(filenev,"wt");


for (i=0;i<i_max;i++)
{

stepsize=2.0*k_edge/((double)i_max);

k=-1*k_edge+i*stepsize;

//pearson7 in fityk
//height/(1+((x-center)/hwhm)^2*(2^(1/shape)-1))^shape

if (k<0)
{
p=1/pow((1+pow(((k-0)/left_hwhm),2)*(pow(2,(1/left_shape))-1)),left_shape);
}
else
{
p=1/pow((1+pow(((k-0)/right_hwhm),2)*(pow(2,(1/right_shape))-1)),right_shape);
}

fprintf(profile,"%.10lg\t",k); fprintf(profile,"%.10lg\n",p);

}

fclose(profile);

}
