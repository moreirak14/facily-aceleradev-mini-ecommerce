from pydantic import BaseSettings


class Settings(BaseSettings):
  app_name: str
  db_username: str
  db_password: str
  db_port: str
  db_name: str

  @property
  def db_url(self):
    return f'postgresql://{self.db_username}:{self.db_password}@db:{self.db_port}/{self.db_name}'


settings = Settings()
