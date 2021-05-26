#!/bin/bash

#############################################################################################################################
#							Author: Mehdi Zare						    #
#							Date  : 11/16/2019 at U of South Carolina			    #
#                                                      Purpose: To assigne charges to the FIELD file                        #
# 				It needs files FIELD_TEMPLATE and DDEC6_even_tempered_net_atomic_charges.xyz  		    #					                    #
#############################################################################################################################


# Check for FIELD_TEMPLATE
if [ ! -f 'FIELD_TEMPLATE' ]; then echo I need file named FIELD_TEMPLATE; exit 1; fi
# Check for CHARGES
if [ ! -f 'DDEC6_even_tempered_net_atomic_charges.xyz' ]; then echo I need file named DDEC6_even_tempered_net_atomic_charges.xyz; exit 1; fi

atoms=`head -1 DDEC6_even_tempered_net_atomic_charges.xyz`
header=2
sum=$(($atoms+$header))
head -n$sum  DDEC6_even_tempered_net_atomic_charges.xyz | tail -n$atoms > CHARGES

cp FIELD_TEMPLATE FIELD

tot=`wc -l CHARGES  | awk '{print $1}'`

line=1
while [ $line -le $tot  ]; do
  chg=`head -n$line CHARGES | tail -1 | awk '{ print $5 }'`
  if [ $line -lt 10  ]; then 
 	 if [  $(echo "$chg < 0" | bc) -eq 1 ]; then
		  sed -i "s/MMS_ATOM_00000$line/$chg/g" FIELD
 	 else
		  sed -i "s/MMS_ATOM_00000$line/ $chg/g" FIELD
  	 fi
  elif [ $line -ge 10 -a $line -lt 100  ]; then
         if [  $(echo "$chg < 0" | bc) -eq 1 ]; then
                  sed -i "s/MMS_ATOM_0000$line/$chg/g" FIELD
         else
                  sed -i "s/MMS_ATOM_0000$line/ $chg/g" FIELD
         fi
   else
         if [  $(echo "$chg < 0" | bc) -eq 1 ]; then
                  sed -i "s/MMS_ATOM_000$line/$chg/g" FIELD
         else
                  sed -i "s/MMS_ATOM_000$line/ $chg/g" FIELD
         fi
   fi
line=$(($line+1));
done

