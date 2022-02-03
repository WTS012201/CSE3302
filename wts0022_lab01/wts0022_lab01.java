import java.util.Scanner;
import java.io.File;

public class wts0022_lab01{
    public static int getSize(String path){
        File dir = new File(path);
        int total = 0;

        for (String elem : dir.list()){
            File f = new File(path + "/" + elem);
            if(f.isFile())
                total += f.length();
            else
                total += getSize(path + "/" + elem);
        }
        return total;
    }
    public static void main(String[] args){
        String currentDir = System.getProperty("user.dir");
        System.out.println(getSize(currentDir) + " bytes");
    }
}