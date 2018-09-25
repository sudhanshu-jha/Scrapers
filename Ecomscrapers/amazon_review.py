from lxml import html 
import requests
import json
asin = 'B0718Y23CQ'
page_response = requests.get('https://www.amazon.com/product-reviews/'+ asin)
parser = html.fromstring(page_response.content)
reviews_html = parser.xpath('//div[@class="a-section review"]')
reviews_arr = []
for review in reviews_html:
    review_dic = {}
    review_dic['title'] = review.xpath('.//a[@data-hook="review-title"]/text()')
    review_dic['rating'] = review.xpath('.//a[@class="a-link-normal"]/@title')
    review_dic['author'] = review.xpath('.//a[@data-hook="review-author"]/text()')
    review_dic['date'] = review.xpath('.//span[@data-hook="review-date"]/text()')
    review_dic['purchase'] = review.xpath('.//span[@data-hook="avp-badge"]/text()')
    review_dic['review_text'] = review.xpath('.//span[@data-hook="review-body"]/text()')
    review_dic['review image'] = review.xpath('//span[@data-hook="R35Y8VYKS43M66_imageSection_main"]')
    review_dic['helpful_votes'] = review.xpath('.//span[@data-hook="helpful-vote-statement"]/text()')
    reviews_arr.append(review_dic)
print(json.dumps(reviews_arr, indent = 4))
