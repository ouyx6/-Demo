# -*- coding:utf-8 -*-
import scrapy

class ShiyanlouCoursesSpider(scrapy.Spider):
    
    name = 'shiyanlou-courses'

    def start_urls(self):
        url_list = ['https://www.shiyanlou.com/courses/',
                'https://www.shiyanlou.com/courses/?page=2',
                'https://www.shiyanlou.com/courses/?page=3']
        return url_list

    def parse(self, response):
        for course in response.css('div.col-md-3'):
            yield {
                    'name': course.css('h6.course-name:text').extract_first().strip(),
                    'description':course.css('div.course-discripton::text').extract_first().strip(),
                    'type': course.css('span.course-type::text').extract_first()
                    'student': course.css('span.students-count span::text').extract_first()
                    }



