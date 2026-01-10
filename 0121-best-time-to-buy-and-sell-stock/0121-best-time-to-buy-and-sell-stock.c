int maxProfit(int* prices, int pricesSize) {
    int mp=0;
    int min=prices[0];
    for(int i=1;i<pricesSize;i++){
        if(prices[i]<min){
            min=prices[i];
        }
        else{
            int cp=prices[i]-min;
            if(cp>mp)
            mp=cp;
        } 
    }

    return mp;
}