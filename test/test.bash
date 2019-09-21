if [[ $CIRCLECI == 'true' ]]
then
DIR=/home/circleci/project
else
DIR=/root/unspendable
fi

CMD=$DIR/unspendable.py
T=DDDDDDDDDDD
(
$CMD 1 $T 
$CMD 9 $T
$CMD mv $T 
$CMD DC $T
)  | sum | grep 52917
