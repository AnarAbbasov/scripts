#include <stdio.h>
#include <threads.h>

#include <curl/curl.h>

int main()
{
    int n=2;
    
   
   
   
   
    CURL *curl=curl_easy_init();
    
    if(curl) {
  CURLcode res;
  curl_easy_setopt(curl, CURLOPT_URL, "https://example.com");
  res = curl_easy_perform(curl);
   printf("%d",res);
  curl_easy_cleanup(curl);

}
    
  

    printf ("hi %d hi %d hello",n,n+n);
}
