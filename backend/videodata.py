from services.videoinsert import VideoData

# from sqlalchemy import create_engine
videos = [
    {
        # 1
        'youtubeId': 'https://youtu.be/OI5BA60PhQI',
        'name': 'Intro to Etsy Essentials',
        'series': 'Etsy Essentials',
        'module': 1
    },
    {
        # 2
        'youtubeId': 'https://youtu.be/lYK3m0RsdH8',
        'name': 'Your Shop Name & Tagline',
        'series': 'Etsy Essentials',
        'module': 1
    },
    {
        # 3
        'youtubeId': 'https://youtu.be/6r3ixttuyUo',
        'name': 'Info & Appearance of Your Etsy Shop',
        'series': 'Etsy Essentials',
        'module': 1
    },
    {
        # 4
        'youtubeId': 'https://youtu.be/B17C1KnxV-E',
        'name': 'Your About Section',
        'series': 'Etsy Essentials',
        'module': 1
    },
    {
        # 5
        'youtubeId': 'https://youtu.be/yq18ltpoKq4',
        'name': 'All about Listing Sections',
        'series': 'Etsy Essentials',
        'module': 1
    },
    {
        # 6
        'youtubeId': 'https://youtu.be/CzCNaFBVGMI',
        'name': 'Shop Layout & Organization',
        'series': 'Etsy Essentials',
        'module': 1
    },
    {
        # 7
        'youtubeId': 'https://youtu.be/9IHOSyrYiPs',
        'name': 'Creating Synergy in Your Shop',
        'series': 'Etsy Essentials',
        'module': 1
    },
    {
        # 8
        'youtubeId': 'https://youtu.be/hTs_rxc791E',
        'name': "Etsy's Search Algorithm",
        'series': 'Etsy Essentials',
        'module': 2
    },
    {
        # 9
        'youtubeId': 'https://youtu.be/IY4T8n-VdFM',
        'name': 'Tools for Etsy SEO',
        'series': 'Etsy Essentials',
        'module': 2
    },
    {
        # 10
        'youtubeId': 'https://youtu.be/IgSxIB3gESs',
        'name': 'Listings Part 1: Tags & Titles',
        'series': 'Etsy Essentials',
        'module': 2
    },
    {
        # 11
        'youtubeId': 'https://youtu.be/XITIM5zegE0',
        'name': 'Listings Part 2: Categories & Attributes',
        'series': 'Etsy Essentials',
        'module': 2
    },
    {
        # 12
        'youtubeId': 'https://youtu.be/uFEspLJf2h8',
        'name': 'Listings Part 3: Descriptions',
        'series': 'Etsy Essentials',
        'module': 2
    },
    {
        # 13
        'youtubeId': 'https://youtu.be/YK8H_hE5eJM',
        'name': 'Listings Part 4: Other Key Elements',
        'series': 'Etsy Essentials',
        'module': 2
    },
    {
        # 14
        'youtubeId': 'https://youtu.be/d0wSWgrumi8',
        'name': 'When to List, Renew, & Deactivate Listings',
        'series': 'Etsy Essentials',
        'module': 2
    },
    {
        # 15
        'youtubeId': 'https://youtu.be/TtrZqXh8XU0',
        'name': 'Introduction to Product Photography',
        'series': 'Etsy Essentials',
        'module': 3
    },
    {
        # 16
        'youtubeId': 'https://youtu.be/f0nZOrsyG0g',
        'name': 'Planning a Photoshoot',
        'series': 'Etsy Essentials',
        'module': 3
    },
    {
        # 17
        'youtubeId': 'https://youtu.be/mwT5tago9FI',
        'name': 'Defining Your Visual Style',
        'series': 'Etsy Essentials',
        'module': 3
    },
    {
        # 18
        'youtubeId': 'https://youtu.be/bLGjeIEpqH0',
        'name': 'A Crash Course in Graphic Design',
        'series': 'Etsy Essentials',
        'module': 3
    },
    {
        # 19
        'youtubeId': 'https://youtu.be/LDi6vopntiw',
        'name': 'Examples of Good & Bad Graphic Design',
        'series': 'Etsy Essentials',
        'module': 3
    },
    {
        # 20
        'youtubeId': 'https://youtu.be/y_h7H9Og80Y',
        'name': 'Pricing Your Products',
        'series': 'Etsy Essentials',
        'module': 4
    },
    {
        # 21
        'youtubeId': 'https://youtu.be/_Up1WosNMw4',
        'name': 'Using the Pricing Worksheet',
        'series': 'Etsy Essentials',
        'module': 4
    },
    {
        # 22
        'youtubeId': 'https://youtu.be/1zgheq7B_IY',
        'name': 'Packaging & Shipping Basics',
        'series': 'Etsy Essentials',
        'module': 4
    },
    {
        # 23
        'youtubeId': 'https://youtu.be/jJZs4o5HTvY',
        'name': 'Shipping Very Large & Very Small Items',
        'series': 'Etsy Essentials',
        'module': 4
    },
    {
        # 24
        'youtubeId': 'https://youtu.be/ItGxe_RKZJA',
        'name': 'Using Shipping Profiles',
        'series': 'Etsy Essentials',
        'module': 4
    },
    {
        # 25
        'youtubeId': 'https://youtu.be/Pr0PJTm-fFk',
        'name': 'Etsy Shipping Walkthrough',
        'series': 'Etsy Essentials',
        'module': 4
    },
    {
        # 26
        'youtubeId': 'https://youtu.be/3m0JHso9-1g',
        'name': 'Customer Service 101',
        'series': 'Etsy Essentials',
        'module': 5
    },
    {
        # 27
        'youtubeId': 'https://youtu.be/je09WTz25dw',
        'name': 'Writing Great Etsy Convos',
        'series': 'Etsy Essentials',
        'module': 5
    },
    {
        # 28
        'youtubeId': 'https://youtu.be/VxHtyN4DVL4',
        'name': 'Dealing with Bad Reviews',
        'series': 'Etsy Essentials',
        'module': 5
    },
    {
        # 29
        'youtubeId': 'https://youtu.be/CuwlnFnO7R8',
        'name': 'Setting Good Boundaries',
        'series': 'Etsy Essentials',
        'module': 5
    },
    {
        # 30
        'youtubeId': 'https://youtu.be/LQJbewLQDmM',
        'name': 'Bonus 1: No Sales? Look at Your Stats',
        'series': 'Etsy Essentials',
        'module': 6
    },
    {
        # 31
        'youtubeId': 'https://youtu.be/qClSzjjVQJQ',
        'name': 'Bonus 2: Some Marketing Options',
        'series': 'Etsy Essentials',
        'module': 6
    },
    {
        # 32
        'youtubeId': 'https://youtu.be/bJVUgrlosxM',
        'name': 'Introduction to Etsy Expert',
        'series': 'Etsy Expert',
        'module': 1
    },
    {
        # 33
        'youtubeId': 'https://youtu.be/ESGBO-NHz_Y',
        'name': 'Expert Course Overview',
        'series': 'Etsy Expert',
        'module': 1
    },
    {
        # 34
        'youtubeId': 'https://youtu.be/9jTwEnr0Cxk',
        'name': 'Keywords 2.0',
        'series': 'Etsy Expert',
        'module': 1
    },
    {
        # 35
        'youtubeId': 'https://youtu.be/h9NWTchyJg0',
        'name': 'Google Adwords',
        'series': 'Etsy Expert',
        'module': 1
    },
    {
        # 36
        'youtubeId': 'https://youtu.be/U_17xS21NZI',
        'name': 'Keywords with Moz',
        'series': 'Etsy Expert',
        'module': 1
    },
    {
        # 37
        'youtubeId': 'https://youtu.be/UgiPYMKyZdk',
        'name': 'Getting Organized with Keywords',
        'series': 'Etsy Expert',
        'module': 1
    },
    {
        # 38
        'youtubeId': 'https://youtu.be/oobr1TkWpmM',
        'name': 'Honing Your Listing Description',
        'series': 'Etsy Expert',
        'module': 1
    },
    {
        # 39
        'youtubeId': 'https://youtu.be/3ScVi7PoSsk',
        'name': 'Why Writing is Essential to Growth',
        'series': 'Etsy Expert',
        'module': 1
    },
    {
        # 40
        'youtubeId': 'https://youtu.be/H69aVBJW0YM',
        'name': 'Copywriting 101',
        'series': 'Etsy Expert',
        'module': 1
    },
    {
        # 41
        'youtubeId': 'https://youtu.be/_nCMG9Zxttc',
        'name': 'More Content Tips',
        'series': 'Etsy Expert',
        'module': 1
    },
    {
        # 42
        'youtubeId': 'https://youtu.be/Pdkad1r7L1A',
        'name': 'Intro to Sales, Coupons, & Targeted Ads',
        'series': 'Etsy Expert',
        'module': 1
    },
    {
        # 43
        'youtubeId': 'https://youtu.be/uHFy-aEjly8',
        'name': 'How to Leverage Sales to Sell More Product',
        'series': 'Etsy Expert',
        'module': 1
    },
    {
        # 44
        'youtubeId': 'https://youtu.be/-MatGcXCgbM',
        'name': 'Enticing Buyers with Coupon Codes',
        'series': 'Etsy Expert',
        'module': 1
    },
    {
        # 45
        'youtubeId': 'https://youtu.be/F7475xY_7Gw',
        'name': 'Closing the Deal with Targeted Campaigns',
        'series': 'Etsy Expert',
        'module': 1
    },
    {
        # 46
        'youtubeId': 'https://youtu.be/C4KAbmn8hVI',
        'name': 'Introduction to Paid Advertising',
        'series': 'Etsy Expert',
        'module': 1
    },
    {
        # 47
        'youtubeId': 'https://youtu.be/pOc0K_XXJ-8',
        'name': 'When to Start Advertising',
        'series': 'Etsy Expert',
        'module': 1
    },
    {
        # 48
        'youtubeId': 'https://youtu.be/KT708WJ3pZI',
        'name': 'When NOT to Pay for Ads',
        'series': 'Etsy Expert',
        'module': 1
    },
    {
        # 49
        'youtubeId': 'https://youtu.be/Mb_nEgRClYE',
        'name': 'Native Etsy Ads',
        'series': 'Etsy Expert',
        'module': 1
    },
    {
        # 50
        'youtubeId': 'https://youtu.be/mV7q4ZZC-lk',
        'name': 'Pitfalls of Native Etsy Ads',
        'series': 'Etsy Expert',
        'module': 1
    },
    {
        # 51
        'youtubeId': 'https://youtu.be/DKVW6Ewi2mA',
        'name': 'Who Benefits from Etsy Ads',
        'series': 'Etsy Expert',
        'module': 1
    },
    {
        # 52
        'youtubeId': 'https://youtu.be/WPi5ybPi6Bs',
        'name': 'Introduction to Offsite Ads',
        'series': 'Etsy Expert',
        'module': 1
    },
    {
        # 53
        'youtubeId': 'https://youtu.be/gKoWCRBkT2s',
        'name': 'Benefits of Offsite Ads',
        'series': 'Etsy Expert',
        'module': 1
    },
    {
        # 54
        'youtubeId': 'https://youtu.be/m95rl3t1vYQ',
        'name': 'Intro to Module 2',
        'series': 'Etsy Expert',
        'module': 2
    },
    {
        # 55
        'youtubeId': 'https://youtu.be/6W42msQhuRo',
        'name': 'Why Aesthetic & Branding Matter',
        'series': 'Etsy Expert',
        'module': 2
    },
    {
        # 56
        'youtubeId': 'https://youtu.be/2mE8nEzbd44',
        'name': 'Real Strategies to Hone Your Aesthetic',
        'series': 'Etsy Expert',
        'module': 2
    },
    {
        # 57
        'youtubeId': 'https://youtu.be/wDuUYEoAbb8',
        'name': 'Shop Cohesion Part 1',
        'series': 'Etsy Expert',
        'module': 2
    },
    {
        # 58
        'youtubeId': 'https://youtu.be/7sUCOBZOwVY',
        'name': 'Shop Cohesion Part 2',
        'series': 'Etsy Expert',
        'module': 2
    },
    {
        # 59
        'youtubeId': 'https://youtu.be/LC5T59fh6lY',
        'name': 'Using All YOur Image Slots to Entice Buyers',
        'series': 'Etsy Expert',
        'module': 2
    },
    {
        # 60
        'youtubeId': 'https://youtu.be/B_x0-VBJ1X0',
        'name': 'Cohesion Pitfalls',
        'series': 'Etsy Expert',
        'module': 2
    },
    {
        # 61
        'youtubeId': 'https://youtu.be/TQOXBhYHSbQ',
        'name': 'Image Design Tips',
        'series': 'Etsy Expert',
        'module': 2
    },
    {
        # 62
        'youtubeId': 'https://youtu.be/SzY-cbaTet0',
        'name': 'Using Color in Design',
        'series': 'Etsy Expert',
        'module': 2
    },
    {
        # 63
        'youtubeId': 'https://youtu.be/JA_QNc2SG-8',
        'name': 'Tools for Design',
        'series': 'Etsy Expert',
        'module': 2
    },
    {
        # 64
        'youtubeId': 'https://youtu.be/1kh-gVv1wu4',
        'name': 'Best Practices for Advertising',
        'series': 'Etsy Expert',
        'module': 2
    },
    {
        # 65
        'youtubeId': 'https://youtu.be/zMhobg_Yvek',
        'name': 'Tips for Social Advertising',
        'series': 'Etsy Expert',
        'module': 2
    },
    {
        # 66
        'youtubeId': 'https://youtu.be/jTrkK6B9PPc',
        'name': 'Best Social Platforms for Ads',
        'series': 'Etsy Expert',
        'module': 2
    },
    {
        # 67
        'youtubeId': 'https://youtu.be/VqZnRIG66lM',
        'name': 'Advertising with Influencers',
        'series': 'Etsy Expert',
        'module': 2
    },
    {
        # 68
        'youtubeId': 'https://youtu.be/Vn0-T3iTUHU',
        'name': 'Native Content Advertising',
        'series': 'Etsy Expert',
        'module': 2
    },
    {
        # 69
        'youtubeId': 'https://youtu.be/5Y1X9xy_FKY',
        'name': 'Google Ads',
        'series': 'Etsy Expert',
        'module': 2
    },
    {
        # 70
        'youtubeId': 'https://youtu.be/Xn9qk-XpuiM',
        'name': 'Outsourcing Your Advertising',
        'series': 'Etsy Expert',
        'module': 2
    },
    {
        # 71
        'youtubeId': 'https://youtu.be/NhBbziZRVYc',
        'name': 'Intro to Free & Almost Free Ad Opportunities',
        'series': 'Etsy Expert',
        'module': 2
    },
    {
        # 72
        'youtubeId': 'https://youtu.be/B_udyJ6MJTo',
        'name': 'Social Media Overview',
        'series': 'Etsy Expert',
        'module': 2
    },
    {
        # 73
        'youtubeId': 'https://youtu.be/_RGdspLhEss',
        'name': 'Pick Two Social Platforms',
        'series': 'Etsy Expert',
        'module': 2
    },
    {
        # 74
        'youtubeId': 'https://youtu.be/ng-qfzAaHFY',
        'name': 'When and What to Post on Social Channels',
        'series': 'Etsy Expert',
        'module': 2
    },
    {
        # 75
        'youtubeId': 'https://youtu.be/rntyT4Iy5uo',
        'name': 'How to Grow Your Social Following',
        'series': 'Etsy Expert',
        'module': 2
    },
    {
        # 76
        'youtubeId': 'https://youtu.be/QndY1AWMwMI',
        'name': 'Engaging with Customers on Social',
        'series': 'Etsy Expert',
        'module': 2
    },
    {
        # 77
        'youtubeId': 'https://youtu.be/plLO_pu3NO0',
        'name': 'Quick Reference Guide to Social',
        'series': 'Etsy Expert',
        'module': 2
    },
    {
        # 78
        'youtubeId': 'https://youtu.be/DsITIrfCb64',
        'name': 'Other Social Platforms to Consider',
        'series': 'Etsy Expert',
        'module': 2
    },
    {
        # 79
        'youtubeId': 'https://youtu.be/xvnywYTsSHI',
        'name': 'Email Marketing Introduction',
        'series': 'Etsy Expert',
        'module': 2
    },
    {
        # 80
        'youtubeId': 'https://youtu.be/SG1OJUPKZeY',
        'name': 'Email Opt-in Ideas',
        'series': 'Etsy Expert',
        'module': 2
    },
    {
        # 81
        'youtubeId': 'https://youtu.be/tkJcCmTeoVw',
        'name': 'Good Email Content',
        'series': 'Etsy Expert',
        'module': 2
    },
    {
        # 82
        'youtubeId': 'https://youtu.be/m-r8vEnz2DU',
        'name': 'Tips for Email Marketing Success',
        'series': 'Etsy Expert',
        'module': 2
    },
    {
        # 83
        'youtubeId': 'https://youtu.be/zIlZVDTWEtA',
        'name': 'More Email Marketing Tips',
        'series': 'Etsy Expert',
        'module': 2
    },
    {
        # 84
        'youtubeId': 'https://youtu.be/5knzHcFprbs',
        'name': 'Measuring the Success of Your Email Marketing Campaign',
        'series': 'Etsy Expert',
        'module': 2
    },
    {
        # 85
        'youtubeId': 'https://youtu.be/M9NAt5QWE14',
        'name': 'More Tools for Email Marketing',
        'series': 'Etsy Expert',
        'module': 2
    },
    {
        # 86
        'youtubeId': 'https://youtu.be/T0wwC--Bbc8',
        'name': 'To Blog or Not',
        'series': 'Etsy Expert',
        'module': 2
    },
    {
        # 87
        'youtubeId': 'https://youtu.be/wwb65vAVaRs',
        'name': 'Module 3 Introduction',
        'series': 'Etsy Expert',
        'module': 3
    },
    {
        # 88
        'youtubeId': 'https://youtu.be/1A3qjI7iq6s',
        'name': 'Using Etsy Analytics',
        'series': 'Etsy Expert',
        'module': 3
    },
    {
        # 89
        'youtubeId': 'https://youtu.be/e8W_Y63CSAs',
        'name': 'Interpreting Your Etsy Stats Data',
        'series': 'Etsy Expert',
        'module': 3
    },
    {
        # 90
        'youtubeId': 'https://youtu.be/YhdSZRDXerE',
        'name': 'Downloading Your Shop Data',
        'series': 'Etsy Expert',
        'module': 3
    },
    {
        # 91
        'youtubeId': 'https://youtu.be/JOx0fCUuyJE',
        'name': 'Google Analytics Basics',
        'series': 'Etsy Expert',
        'module': 3
    },
    {
        # 92
        'youtubeId': 'https://youtu.be/VWlNUMfxN8s',
        'name': 'Social Media Analytics',
        'series': 'Etsy Expert',
        'module': 3
    },
    {
        # 93
        'youtubeId': 'https://youtu.be/lH-5p5cpx2I',
        'name': 'Pattern Part 1',
        'series': 'Etsy Expert',
        'module': 3
    },
    {
        # 94
        'youtubeId': 'https://youtu.be/4vdseLTq9fE',
        'name': 'Pattern Part 2',
        'series': 'Etsy Expert',
        'module': 3
    },
    {
        # 95
        'youtubeId': 'https://youtu.be/NAIYCYjV92U',
        'name': 'Introduction to Other E-Commerce Sites',
        'series': 'Etsy Expert',
        'module': 3
    },
    {
        # 96
        'youtubeId': 'https://youtu.be/cLSM1M5uXSI',
        'name': 'SquareSpace',
        'series': 'Etsy Expert',
        'module': 3
    },
    {
        # 97
        'youtubeId': 'https://youtu.be/8V0QIXNrE2c',
        'name': 'Shopify',
        'series': 'Etsy Expert',
        'module': 3
    },
    {
        # 98
        'youtubeId': 'https://youtu.be/efTulNNUYJI',
        'name': 'Amazon',
        'series': 'Etsy Expert',
        'module': 3
    },
    {
        # 99
        'youtubeId': 'https://youtu.be/9SsPyBuyom8',
        'name': 'Using All the Platforms',
        'series': 'Etsy Expert',
        'module': 3
    },
    {
        # 100
        'youtubeId': 'https://youtu.be/-Iw5D7vBgI8',
        'name': 'What to do if Sales Stall',
        'series': 'Etsy Expert',
        'module': 3
    },
    {
        # 101
        'youtubeId': 'https://youtu.be/cGbHLrBjXYI',
        'name': 'More Tips for Sale Stalls',
        'series': 'Etsy Expert',
        'module': 3
    },
    {
        # 102
        'youtubeId': 'https://youtu.be/UcAayGwWS-Q',
        'name': 'Renewing Your Listings to Increase Sales',
        'series': 'Etsy Expert',
        'module': 3
    },
    {
        # 103
        'youtubeId': 'https://youtu.be/6zozdf4gxCE',
        'name': 'Reasons Sales Might Slow Down',
        'series': 'Etsy Expert',
        'module': 3
    },
    {
        # 104
        'youtubeId': 'https://youtu.be/eSn84syFf4Y',
        'name': 'Module 4 Overview',
        'series': 'Etsy Expert',
        'module': 4
    },
    {
        # 105
        'youtubeId': 'https://youtu.be/gCtop4_umy4',
        'name': 'Having a Growth Mindset',
        'series': 'Etsy Expert',
        'module': 4
    },
    {
        # 106
        'youtubeId': 'https://youtu.be/4qMOueUHzx0',
        'name': 'Signs You are Growing',
        'series': 'Etsy Expert',
        'module': 4
    },
    {
        # 107
        'youtubeId': 'https://youtu.be/ySqxaWPtD0s',
        'name': 'The Big 3 of Scaling',
        'series': 'Etsy Expert',
        'module': 4
    },
    {
        # 108
        'youtubeId': 'https://youtu.be/qZLgf_coZW0',
        'name': 'All About LLCs',
        'series': 'Etsy Expert',
        'module': 4
    },
    {
        # 109
        'youtubeId': 'https://youtu.be/4zkMLAo1fAE',
        'name': 'All About S-Corps',
        'series': 'Etsy Expert',
        'module': 4
    },
    {
        # 110
        'youtubeId': 'https://youtu.be/XRwpQUUNGh8',
        'name': 'Changing Your Business Structure',
        'series': 'Etsy Expert',
        'module': 4
    },
    {
        # 111
        'youtubeId': 'https://youtu.be/UyDSZik59gM',
        'name': 'Overview of Accounting',
        'series': 'Etsy Expert',
        'module': 4
    },
    {
        # 112
        'youtubeId': 'https://youtu.be/pwVOSDg8iSU',
        'name': 'Expense Tracking',
        'series': 'Etsy Expert',
        'module': 4
    },
    {
        # 113
        'youtubeId': 'https://youtu.be/PbW3_j4l794',
        'name': 'Invoicing & Time Tracking Software',
        'series': 'Etsy Expert',
        'module': 4
    },
    {
        # 114
        'youtubeId': 'https://youtu.be/fKauxUkKruA',
        'name': 'Creating a Business Plan',
        'series': 'Etsy Expert',
        'module': 4
    },
    {
        # 115
        'youtubeId': 'https://youtu.be/yYzq6VvwMnQ',
        'name': 'Getting a Business License',
        'series': 'Etsy Expert',
        'module': 4
    },
    {
        # 116
        'youtubeId': 'https://youtu.be/JAyb7-og_ew',
        'name': 'Getting a Dedicated Workspace',
        'series': 'Etsy Expert',
        'module': 4
    },
    {
        # 117
        'youtubeId': 'https://youtu.be/8-QHOBf3oM8',
        'name': 'More Studio Logistics',
        'series': 'Etsy Expert',
        'module': 4
    },
    {
        # 118
        'youtubeId': 'https://youtu.be/419ksfFaJDo',
        'name': 'Hiring Help',
        'series': 'Etsy Expert',
        'module': 4
    },
    {
        # 119
        'youtubeId': 'https://youtu.be/qFG_k_xaDE4',
        'name': 'Best Practices in Hiring',
        'series': 'Etsy Expert',
        'module': 4
    },
    {
        # 120
        'youtubeId': 'https://youtu.be/A9ZGaY0OvP4',
        'name': 'Next-Level Shipping',
        'series': 'Etsy Expert',
        'module': 4
    },
    {
        # 121
        'youtubeId': 'https://youtu.be/pWj0TsVyxVo',
        'name': 'More Pro Shipping Tips',
        'series': 'Etsy Expert',
        'module': 4
    },
    {
        # 122
        'youtubeId': 'https://youtu.be/mxicHsj_VS4',
        'name': 'Shipping Life Lessons',
        'series': 'Etsy Expert',
        'module': 4
    },
    {
        # 123
        'youtubeId': 'https://youtu.be/DL-EN5TO2Vc',
        'name': 'Supply Chain & Growth',
        'series': 'Etsy Expert',
        'module': 4
    },
    {
        # 124
        'youtubeId': 'https://youtu.be/kYk2PvDP02k',
        'name': 'Sourcing Materials for Products',
        'series': 'Etsy Expert',
        'module': 4
    },
    {
        # 125
        'youtubeId': 'https://youtu.be/5v8KNAQbVss',
        'name': 'Verifying Product Quality',
        'series': 'Etsy Expert',
        'module': 4
    },
    {
        # 126
        'youtubeId': 'https://youtu.be/yvdeounZ1k0',
        'name': 'Drop Shipping & White Labels',
        'series': 'Etsy Expert',
        'module': 4
    },
    {
        # 127
        'youtubeId': 'https://youtu.be/g-aZHYsU1II',
        'name': 'Wholesale vs. Consignment',
        'series': 'Etsy Expert',
        'module': 4
    },
    {
        # 128
        'youtubeId': 'https://youtu.be/Qhqz5NqJmSw',
        'name': 'Introduction to Module 5',
        'series': 'Etsy Expert',
        'module': 5
    },
    {
        # 129
        'youtubeId': 'https://youtu.be/J-4yJIXmHP0',
        'name': 'Copycats',
        'series': 'Etsy Expert',
        'module': 5
    },
    {
        # 130
        'youtubeId': 'https://youtu.be/LyBG0pYuqo8',
        'name': 'Iterating Small with New Products',
        'series': 'Etsy Expert',
        'module': 5
    },
    {
        # 131
        'youtubeId': 'https://youtu.be/PK3IwNg802M',
        'name': 'Testing Market Viability',
        'series': 'Etsy Expert',
        'module': 5
    },
    {
        # 132
        'youtubeId': 'https://youtu.be/R4OoOjwesB8',
        'name': 'Troubleshooting with Etsy Forums',
        'series': 'Etsy Expert',
        'module': 5
    },
    {
        # 133
        'youtubeId': 'https://youtu.be/oiSk9zjXkXU',
        'name': 'Is It Me? Or Is It Etsy?',
        'series': 'Etsy Expert',
        'module': 5
    },
    {
        # 134
        'youtubeId': 'https://youtu.be/YYrISnZnvyA',
        'name': 'How to Contact a Human at Etsy Help',
        'series': 'Etsy Expert',
        'module': 5
    },
    {
        # 135
        'youtubeId': 'https://youtu.be/UyEj8-5Jb4U',
        'name': 'Account Shutdowns and Limitations',
        'series': 'Etsy Expert',
        'module': 5
    },
    {
        # 136
        'youtubeId': 'https://youtu.be/bU5MeNbB7WY',
        'name': 'Should I Use Vacation Mode',
        'series': 'Etsy Expert',
        'module': 5
    },
    {
        # 137
        'youtubeId': 'https://youtu.be/vILuyAGfcS0',
        'name': 'Using Variations',
        'series': 'Etsy Expert',
        'module': 5
    },
    {
        # 138
        'youtubeId': 'https://youtu.be/wrFHHceTSK4',
        'name': 'Get Out There & Etsy',
        'series': 'Etsy Expert',
        'module': 5
    },

]

videoModule = VideoData()


def addVideos():
    for v in videos:
        # print(v["videoId"])
        # vidId = v["videoId"]
        ytId = v["youtubeId"]
        n = v["name"]
        s = v["series"]
        m = v["module"]
        videoModule.addVideoObjects(ytId, n, s, m)


addVideos()


# def removeVideo():
#     videoModule.removeVideoObject(2)


# removeVideo()
