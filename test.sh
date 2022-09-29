set -ex

for i in {1..100}
do
    echo $i
    pytest test_hypothesis.py
done
