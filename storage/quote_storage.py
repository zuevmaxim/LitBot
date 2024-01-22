from dataclasses import dataclass

from dacite import from_dict

from storage.postgres import db


@dataclass(frozen=True)
class Author:
    first_name: str
    last_name: str


@dataclass(frozen=True)
class Source:
    author: Author
    name: str
    year: int


@dataclass(frozen=True)
class Quote:
    quote_id: int
    text: str
    autor_first_name: str
    author_last_name: str
    source: str
    source_year: int

    @staticmethod
    def parse_json(json_data: dict):
        return from_dict(data_class=Quote, data=json_data)


class QuoteStorage:
    @staticmethod
    def add_author(author: Author) -> int:
        db.execute("INSERT INTO Author(first_name, last_name) "
                   "VALUES (%s, %s) ON CONFLICT DO NOTHING", [author.first_name, author.last_name])
        cursor = db.execute("SELECT id FROM Author "
                            "WHERE first_name = %s "
                            "AND last_name = %s", [author.first_name, author.last_name])
        # get id here
        return 1

    @staticmethod
    def add_source(source: Source) -> int:
        author_id = QuoteStorage.add_author(source.author)
        # add source if not exists
        # get and return source id
        pass

    @staticmethod
    def load_quotes(quotes: [str], source: Source):
        source_id = QuoteStorage.add_source(source)
        # add all quotes
        pass

        # db.execute("INSERT INTO Post(post_id, channel_id, timestamp, comments, reactions) "
        #            "VALUES {} ON CONFLICT (post_id, channel_id) DO UPDATE SET "
        #            "comments = excluded.comments, "
        #            "reactions = excluded.reactions, "
        #            "timestamp = excluded.timestamp".format(str_args), args)
