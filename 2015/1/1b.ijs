z =: }:fread 'small.txt'
d =: }:fread 'big.txt'
echo 1++/{.\:0>+/\_1+2*'('=z
echo 1++/{.\:0>+/\_1+2*'('=d
exit 0
