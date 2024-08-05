from src.model.utils import Database


class TestDatabase:
    def test_database(self):
        db = Database()
        conn = db.create_connection()
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS test (id SERIAL PRIMARY KEY, test_val VARCHAR(100))")
        conn.commit()

        cursor.execute(
            """
                SELECT EXISTS (
                    SELECT FROM information_schema.tables
                    WHERE table_name = %s
                );
            """,
            ("test",),
        )
        exists = cursor.fetchone()[0]
        assert exists

        cursor.execute("SELECT * FROM test")
        rows = cursor.fetchall()
        assert len(rows) == 0

        cursor.execute("INSERT INTO test (test_val) VALUES ('test')")
        conn.commit()

        cursor.execute("SELECT * FROM test")
        rows = cursor.fetchall()
        assert len(rows) == 1

        cursor.execute("DELETE FROM test WHERE test_val = 'test'")
        conn.commit()

        cursor.execute("SELECT * FROM test")
        rows = cursor.fetchall()
        assert len(rows) == 0

        cursor.execute("DROP TABLE test")
        conn.commit()
        cursor.execute(
            """
                        SELECT EXISTS (
                            SELECT FROM information_schema.tables
                            WHERE table_name = %s
                        );
                    """,
            ("test",),
        )
        exists = cursor.fetchone()[0]
        assert not exists

        cursor.close()
        conn.close()
