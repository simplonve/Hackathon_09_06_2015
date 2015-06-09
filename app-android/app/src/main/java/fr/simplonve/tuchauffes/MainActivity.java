package fr.simplonve.tuchauffes;

import android.app.Activity;
import android.media.MediaPlayer;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.ImageView;
import android.widget.TextView;


public class MainActivity extends Activity {
    MediaPlayer mp;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mp = MediaPlayer.create(MainActivity.this, R.raw.sample_thierry);
        mp.setLooping(true);
        mp.start();

        final ImageView animRotate = (ImageView) findViewById(R.id.imageRotate);
        animRotate.startAnimation(animRotate);
    }

}
