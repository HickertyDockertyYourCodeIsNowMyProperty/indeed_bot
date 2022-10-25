from userDetails import EMAIL, PASSWORD
from user import User
from webpage import webpage


def main():
    user = User()
    w = webpage()
    w.get_website()
    w.reject_all()
    for keyword in user.keywords:
        w.search(keyword)
        w.sort_by_date()
        for i in range(5):

            w.find_jobs()
            w.click_next_button()

if __name__ == '__main__':
    main()
