# cook_example

This is only a experiment repo, not production ready.

The main code is point/views.py

## Usage

* POST `point/import`
  * Get a post parameter `data` which is a json string of the required data
  * Json Example:

```
[["user1", "3452198438", 10], ["user2", "0987654321", 10], ["user3", "7478349022", 10]]
```

* POST `point/old_import`
  * The same as `point/import`, but the internal behavior is different.
  * Get a post parameter `data` which is a json string of the required data
  * Json Example:

```
[["user1", "3452198438", 10], ["user2", "0987654321", 10], ["user3", "7478349022", 10]]
```
