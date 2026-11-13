
import happybase

def get_hbase_data():
    # Connect to HBase
    connection = happybase.Connection(
        host='127.0.0.1',
        port=9090,
        timeout=10000
    )

    try:
        connection.open()

        # Access the renewable energy table
        table = connection.table('renewable_energy')

        # Retrieve all records
        records = []

        for row_key, data in table.scan():
            record = {
                'row_key': row_key.decode('utf-8')
            }

            for column, value in data.items():
                column_name = column.decode('utf-8').split(':')[1]
                record[column_name] = value.decode('utf-8')

            records.append(record)

        return records

    finally:
        connection.close()


# Test the connection and display records
if __name__ == "__main__":
    data = get_hbase_data()

    print("Successfully retrieved data from HBase!")
    print("Total records:", len(data))

    for record in data:
        print(record)
