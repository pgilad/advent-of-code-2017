legit_part_1=0
while IFS='' read -r line || [[ -n "$line" ]]; do
    highest_1=$(echo $line | tr ' ' '\n' | sort | uniq -c | awk '{print $1}' | sort -r | head -1)
    if [ "$highest_1" -eq 1 ]; then
        ((legit_part_1++))
    fi
done < "day4.txt"

echo "part 1 legit passwords: $legit_part_1"
