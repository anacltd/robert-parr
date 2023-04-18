```

  _____       _               _     _____                
 |  __ \     | |             | |   |  __ \               
 | |__) |___ | |__   ___ _ __| |_  | |__) |_ _ _ __ _ __ 
 |  _  // _ \| '_ \ / _ \ '__| __| |  ___/ _` | '__| '__|
 | | \ \ (_) | |_) |  __/ |  | |_  | |  | (_| | |  | |   
 |_|  \_\___/|_.__/ \___|_|   \__| |_|   \__,_|_|  |_|   
                                                         
                                                         

```

Long story short: my boyfriend reads. A lot. And he likes to learn new words. To keep track of those, he built a Notion database with words he doesn't know the definition of, and he manually go on Le Robert (his favourite dictionary) online to copy-paste the definition.

This repo contains a codebase that retrieves rows from a Notion database, retrieves the definition of a word when it is missing and updates the row with the relevant information.  

DISCLAIMER: this codebase fits **very specific** needs (column names, text formatting...).  
(Also, the name? A reference to Pixar's movie _The Incredibles_)

💡 You'll need a `credentials.conf` file at the root of the repo with the hereunder information:
```
[notion]
secret=your notion app secret
db_id=the id of your database
```