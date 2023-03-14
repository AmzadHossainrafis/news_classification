import pytest 
import os 
import pandas as pd 
from project.config import *
from project.utils import *


expected_out_come='কোম্পানি জানালো পর্ষদ সভার তারিখ: শেয়ারবাজারে তালিকাভুক্ত কোম্পানির পরিচালনা পর্ষদ প্রান্তিক প্রতিবেদন প্রকাশ সংক্রান্ত পরিচালনা পর্ষদ সভার তারিখ ঘোণষা করেছে।বুধবার ঢাকা স্টক এক্সচেঞ্জ সূত্রে তথ্য গেছে। কোম্পানিগুলো হলো- আরএন স্পিনিং, দেশবন্ধু পলিমার, তমিজউদ্দিন টেক্সটাইল, ফার কেমিক্যাল, এমএল ডাইং, মুন্নু সিরামিক, মুন্নু ফেব্রিক্স, মুন্নু এগ্রো রানার অটোমোবাইল।কোম্পানিগুলোর আরএন স্পিনিংয়ের বোর্ড সভা জানুয়ারি বিকাল টায়, দেশবন্ধু পলিমারের জানুয়ারি বিকাল সাড়ে টায়, তমিজউদ্দিন টেক্সটাইলের জানুয়ারি বিকাল সাড়ে টায়, ফার কেমিক্যালের জানুয়ারি বিকাল টায়, এমএল ডাইংয়ের জানুয়ারি বিকাল সাড়ে টায়, মুন্নু সিরামিকের জানুয়ারি সন্ধ্যা টায়, মুন্নু ফেব্রিক্সের জানুয়ারি বিকাল সাড়ে টায়, মুন্নু এগ্রোর জানুয়ারি বিকাল সাড়ে টায় রানার অটোমোবাইলের জানুয়ারি বিকাল টায় অনুষ্ঠিত হবে।কোম্পানিগুলোর বোর্ড সভায় ডিসেম্বর সমাপ্ত ছয় মাসের অনিরীক্ষিত আর্থিক প্রতিবেদন পর্যালোচনা শেয়ারহোল্ডারদের প্রকাশ হবে।'
input_data='৯ কোম্পানি জানালো পর্ষদ সভার তারিখ: শেয়ারবাজারে তালিকাভুক্ত ৯টি কোম্পানির পরিচালনা পর্ষদ তাদের প্রান্তিক প্রতিবেদন প্রকাশ সংক্রান্ত পরিচালনা পর্ষদ সভার তারিখ ঘোণষা করেছে।বুধবার (১৯ জানুয়ারি) ঢাকা স্টক এক্সচেঞ্জ (ডিএসই) সূত্রে এ তথ্য জানা গেছে। কোম্পানিগুলো হলো- আরএন স্পিনিং, দেশবন্ধু পলিমার, তমিজউদ্দিন টেক্সটাইল, ফার কেমিক্যাল, এমএল ডাইং, মুন্নু সিরামিক, মুন্নু ফেব্রিক্স, মুন্নু এগ্রো ও রানার অটোমোবাইল।কোম্পানিগুলোর মধ্যে আরএন স্পিনিংয়ের বোর্ড সভা ২৪ জানুয়ারি বিকাল ৩টায়, দেশবন্ধু পলিমারের ২৪ জানুয়ারি বিকাল সাড়ে ৩টায়, তমিজউদ্দিন টেক্সটাইলের ২৫ জানুয়ারি বিকাল সাড়ে ৩টায়, ফার কেমিক্যালের ২৪ জানুয়ারি বিকাল ৪টায়, এমএল ডাইংয়ের ২৪ জানুয়ারি বিকাল সাড়ে ৩টায়, মুন্নু সিরামিকের ২৫ জানুয়ারি সন্ধ্যা ৬টায়, মুন্নু ফেব্রিক্সের ২৫ জানুয়ারি বিকাল সাড়ে ৪টায়, মুন্নু এগ্রোর ২৫ জানুয়ারি বিকাল সাড়ে ৩টায় এবং রানার অটোমোবাইলের ২৪ জানুয়ারি বিকাল ৩টায় অনুষ্ঠিত হবে।কোম্পানিগুলোর বোর্ড সভায় ৩১ ডিসেম্বর ২০২১ সমাপ্ত ছয় মাসের অনিরীক্ষিত আর্থিক প্রতিবেদন পর্যালোচনা করে তা শেয়ারহোল্ডারদের জন্য প্রকাশ করা হবে।'



def test_preprocess_news(data=input_data,expected_out_come=expected_out_come):
    assert preprocess_news(data,pre_process_config['stop_word']) == expected_out_come

