from credentials import tweet
import schedule

schedule.every().day.at("10:00").do(tweet())


def main():
    tweet()


main()
