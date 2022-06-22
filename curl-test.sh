REQUEST=$(curl -s -X POST http://localhost:5000/api/timeline_post -d'name=Tayeeb&email=tayeeb@gmail.com&content=Just Added Database to my portfolio site!')
RESPONSE=$(curl -s --request GET http://localhost:5000/api/timeline_post | jq '.["timeline_posts"]' | jq '.[]' | jq -j '.name," ",.email," ",.content,"\n"' )
TEST="Tayeeb tayeeb@gmail.com Just Added Database to my portfolio site!"
if [[ "$RESPONSE" == *"$TEST"* ]]; then
        echo "Test passed!"
else
        echo "Test failed!"
fi
