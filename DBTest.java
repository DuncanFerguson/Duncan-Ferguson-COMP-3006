package jdbctest;

import java.sql.*;

public class DBTest {

	public static void main(String[] args) {
		
		String db_url = "jdbc:mysql://localhost/comp3421";
		
		String user = "root";
		String pass = "ilovesql";
		
		try {
			Connection conn = DriverManager.getConnection(db_url, user, pass);
		
			Statement stmt = conn.createStatement();
			
			String sql = "SELECT cust_id, cust_name FROM candy_customer";
			
			ResultSet rs = stmt.executeQuery(sql);
			
			while (rs.next()) {
				
				int cust_id = rs.getInt("cust_id");
				String name = rs.getString("cust_name");
				System.out.println("custID: " + cust_id + ", name " + name);
				
			}
		
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

}
